from datetime import date

from django.db import models
from django.urls import reverse

# Create your models here.



class Album_love(models.Model):
    title = models.CharField('Название альбома', max_length=100)
    album_poster = models.ImageField('Обложка альбома', upload_to='love_story_fotosessiya/')
    # date_album = models.DateField('Дата', default=date.today)
    url = models.SlugField('URL-привязка', max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_love_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Foto_love(models.Model):
    image = models.ImageField('Фотография', upload_to='love_story_photosessiya/albums')
    album = models.ForeignKey(Album_love, verbose_name='Альбом', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.album.title

    class Meta:
        verbose_name= 'Фотография'
        verbose_name_plural= 'Фотографии'
