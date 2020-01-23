from django.db import models
from django.contrib import admin



# Create your models here.

class Fotoset(models.Model):
    name = models.CharField('Вид фотосъёмки', max_length=100, default='СВАДЕБНАЯ ФОТОСЪЁМКА')
    poster_fotoset = models.ImageField('Обложка Свадебной фотосъёмки', upload_to='fotoset_img/')
    description = models.TextField('Короткое описание (для главной)', default='')

    name1 = models.CharField('Вид фотосъёмки', max_length=100, default='LOVE STORY')
    poster_fotoset1 = models.ImageField('Обложка фотосъёмки LOVE STORY', upload_to='fotoset_img/')
    description1 = models.TextField('Короткое описание (для главной)', default='')

    name2 = models.CharField('Вид фотосъёмки', max_length=100, default='СЕМЕЙНАЯ ФОТОСЪЁМКА')
    poster_fotoset2 = models.ImageField('Обложка Семейной фотосъёмки', upload_to='fotoset_img/')
    description2 = models.TextField('Короткое описание (для главной)', default='')

    name3 = models.CharField('Вид фотосъёмки', max_length=100, default='ДЕТСКАЯ ФОТОСЪЁМКА')
    poster_fotoset3 = models.ImageField('Обложка Детской фотосъёмки', upload_to='fotoset_img/')
    description3 = models.TextField('Короткое описание (для главной)', default='')

    name4 = models.CharField('Вид фотосъёмки', max_length=100, default='ИНДИВИДУАЛЬНАЯ ФОТОСЪЁМКА')
    poster_fotoset4 = models.ImageField('Обложка Индивидуальной фотосъёмки', upload_to='fotoset_img/')
    description4 = models.TextField('Короткое описание (для главной)', default='')

    name5 = models.CharField('Вид фотосъёмки', max_length=100, default='ДЕНЬ РОЖДЕНИЯ')
    poster_fotoset5 = models.ImageField('Обложка фотосъёмки Дня рождения', upload_to='fotoset_img/')
    description5 = models.TextField('Короткое описание (для главной)', default='')

    name6 = models.CharField('Вид фотосъёмки', max_length=100, default='НОВОГОДНЯЯ ФОТОСЪЁМКА')
    poster_fotoset6 = models.ImageField('Обложка Новогодней фотосъёмки', upload_to='fotoset_img/')
    description6 = models.TextField('Короткое описание (для главной)', default='')
    updated = models.DateTimeField(auto_now=True)





    # def __str__(self):
    #     return self.name

    def __str__(self):
        return 'Страничка "фотосессии"'

    def image_img(self):
        return self.poster_fotoset



    class Meta:
        verbose_name = 'Страничка "фотосессии"'
        verbose_name_plural = 'Страничка "фотосессии"'


class FotosetAdmin(admin.ModelAdmin):
    list = ('name', 'poster', 'image_img',)



