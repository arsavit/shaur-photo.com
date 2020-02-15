from datetime import date
from django.utils import timezone
import datetime
from django.db import models
from django.urls import reverse

# Create your models here.



class Album(models.Model):
    title = models.CharField('Название альбома', max_length=100)
    album_poster = models.ImageField('Обложка альбома', upload_to='svadebnaya_fotosessiya/')
    # date_album = models.DateField('Дата', default=date.today)
    url = models.SlugField('URL-привязка', max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={"slug": self.url})

    def was_published_recently(self):
        return self.publish >= (timezone.now()-datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ('-publish',)


class Foto(models.Model):
    image = models.ImageField('Фотография', upload_to='svadebnaya_fotosessiya/albums')
    album = models.ForeignKey(Album, verbose_name='Альбом', on_delete=models.CASCADE, default='')
    width = models.CharField('Ширина', max_length=100,  blank=True)

    def __str__(self):
        return self.album.title

    class Meta:
        verbose_name= 'Фотография'
        verbose_name_plural= 'Фотографии'


