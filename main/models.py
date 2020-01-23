from django.db import models

# Create your models here.

class Headers(models.Model):
    head1 = models.CharField('Заголовок для видов фотосессий', max_length=150, default='Популярные виды фотосессий')
    head2 = models.CharField('Заголовок для слайдера', max_length=150, default='Такой-то альбом')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.head1

    class Meta:
        verbose_name_plural = 'Заголовки на главной'
        verbose_name = 'Заголовки на главной'

class Slider_head(models.Model):
    description = models.CharField('Очень короткое описание', max_length=100)
    image = models.ImageField('Изображение для слайдера вверху', upload_to='main_slider')
    head1 = models.ForeignKey(Headers, verbose_name='', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Изображение для слайдера вверху страницы'
        verbose_name_plural = 'Изображения для слайдера вверху страницы'

class Slider_down(models.Model):
    description_sd = models.CharField('Очень короткое описание', max_length=100)
    image_sd = models.ImageField('Изображение для слайдера внизу', upload_to='secons_slider')
    head2 = models.ForeignKey(Headers, verbose_name='', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.description_sd

    class Meta:
        verbose_name = 'Изображение для второго слайдера'
        verbose_name_plural = 'Изображения для второго слайдера'


