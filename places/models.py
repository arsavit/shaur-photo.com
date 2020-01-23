from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse


class Sity(models.Model):
    # Город
    name = models.CharField('Город', max_length=70)
    poster_place = models.ImageField('Изображение', upload_to='city_img/')
    url = models.SlugField(max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sity_detail', kwargs={"slug": self.url})


    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Places(models.Model):
    name = models.CharField('Место', max_length=70)
    description = models.TextField('Описание')
    poster = models.ImageField('Изображение', upload_to='places_img')
    maps = models.CharField('Ссылка на расположение на карте', max_length=300, default='')
    city = models.ForeignKey(Sity, verbose_name='Город', on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.name} - {self.city}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
