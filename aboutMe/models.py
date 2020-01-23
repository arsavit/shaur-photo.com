from django.db import models
from django.urls import reverse


# Create your models here.

class About(models.Model):

    title = models.CharField('Заголовок', max_length=200)
    avatar = models.ImageField('Изображение', upload_to='about_img/')
#    second_title = models.CharField('Заголовок подраздела', max_length=150)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

class Desc(models.Model):

    main_description = models.TextField('Абзац основного раздела')
    about = models.ForeignKey(About, verbose_name='к заголовку', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.main_description

    class Meta:
        verbose_name = 'Абзац основного раздела'
        verbose_name_plural = 'Абзацы основного раздела'


