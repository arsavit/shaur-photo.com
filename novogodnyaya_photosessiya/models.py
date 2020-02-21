from datetime import date
from django.utils import timezone
import datetime
from django.db import models
from django.urls import reverse

# Create your models here.



class Album_nov(models.Model):
    title = models.CharField('Название альбома', max_length=100)
    album_poster = models.ImageField('Обложка альбома', upload_to='novogodnyaya_fotosessiya/')
    # date_album = models.DateField('Дата', default=date.today)
    url = models.SlugField('URL-привязка', max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_nov_detail', kwargs={"slug": self.url})

    def was_published_recently(self):
        return self.publish >= (timezone.now()-datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ('-publish',)

class Foto_nov(models.Model):
    image = models.ImageField('Сжатая фотография', db_index=False,
                              upload_to='novogodnyaya_fotosessiya/albums')
    image_full = models.ImageField('Фото с хорошим качеством', blank=True, db_index=False,
                                   upload_to='novogodnyaya_fotosessiya/albums/low')
    album = models.ForeignKey(Album_nov, verbose_name='Альбом', on_delete=models.CASCADE, default='')
    width = models.CharField('Ширина', db_index=False,  max_length=100,  blank=True)

    def __str__(self):
        return self.album.title

    class Meta:
        verbose_name= 'Фотография'
        verbose_name_plural= 'Фотографии'
