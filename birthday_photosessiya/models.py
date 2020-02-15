from datetime import date

from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


# Create your models here.



class Album_birt(models.Model):
    title = models.CharField('Название альбома', max_length=100)
    album_poster = models.ImageField('Обложка альбома', upload_to='birthday_fotosessiya/')

    url = models.SlugField('URL-привязка', max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_birt_detail', kwargs={"slug": self.url})

    def was_published_recently(self):
        return self.publish >= (timezone.now()-datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ('-publish',)

class Foto_birt(models.Model):
    image = models.ImageField('Фотография', upload_to='birthday_photosessiya/albums')
    album = models.ForeignKey(Album_birt, verbose_name='Альбом', on_delete=models.CASCADE, default='')
    width = models.CharField('Ширина', max_length=100,  blank=True)

    def __str__(self):
        return self.album.title

    class Meta:
        verbose_name= 'Фотография'
        verbose_name_plural= 'Фотографии'
