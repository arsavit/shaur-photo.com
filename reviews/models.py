from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField('Имя автора отзыва', max_length=100)
    avatar = models.ImageField('Аватар автора отзыва', upload_to='reviews_autor')
    social_url = models.CharField('Ссылка на страничку в соц. сетях автора', max_length=250)
    proof_url = models.CharField('Ссылка на сам отзыв в группе', max_length=250)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор отзыва'
        verbose_name_plural = 'Авторы отзывов'

class Body(models.Model):
    description = models.TextField('Абзац отзыва')
    autor = models.ForeignKey(Autor, verbose_name='Автор отзыва', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Абзац отзыва'
        verbose_name_plural = 'Абзацы отзыва'

class Foto(models.Model):
    description_foto_rev = models.TextField('Очень короткое описание фото', max_length=50)
    image = models.ImageField('Фото к отзыву', upload_to='reviews_images')
    autor = models.ForeignKey(Autor, verbose_name='Автор отзыва', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.description_foto_rev

    class Meta:
        verbose_name_plural = 'Фотографии к отзыву'
        verbose_name = 'Фотография к отзыву'
