from django.db import models
from django.urls import reverse
# Create your models here.




class Price(models.Model):
    #
    name = models.CharField('Вид фотосъёмки', max_length=200)
    poster_price = models.ImageField('Изображение фотосъёмки', upload_to='price_img/')
    url = models.SlugField('URL-привязка', max_length=50, unique=True)

    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('price_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Вид фотосъёмки'
        verbose_name_plural = 'Виды фотосъёмок'

class Price_Description(models.Model):

    description = models.TextField('Описание фотосъёмки для раздела "Прайс"')
    price = models.ForeignKey(Price, verbose_name='Вид фотосъёмки', on_delete=models.CASCADE, default='')
    def __str__(self):
        # return f'{self.description} - {self.price}'
        return self.description

    class Meta:
        verbose_name = 'Абзац описания фотосъёмки'
        verbose_name_plural = 'Абзацы описания фотосъёмки'

class Tariffs(models.Model):

    title = models.CharField('Название тарифа', max_length=200)
    tariffs_description = models.TextField('Описание тарифа')
    tariffs_price = models.CharField('Цена тарифа с указанием валюты', max_length=100)
    price_tar = models.ForeignKey(Price, verbose_name='Тариф', on_delete=models.CASCADE, default='')

    def __str__(self):
        # return f'{self.title} - {self.price_tar}'
        return self.title

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


