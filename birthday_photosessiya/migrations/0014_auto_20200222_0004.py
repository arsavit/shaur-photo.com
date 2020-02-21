# Generated by Django 3.0.1 on 2020-02-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_photosessiya', '0013_auto_20200220_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto_birt',
            name='image_low',
        ),
        migrations.AddField(
            model_name='foto_birt',
            name='image_full',
            field=models.ImageField(blank=True, upload_to='birthday_fotosessiya/albums/low', verbose_name='Фото с хорошим качеством'),
        ),
        migrations.AlterField(
            model_name='foto_birt',
            name='image',
            field=models.ImageField(upload_to='birthday_fotosessiya/albums', verbose_name='Сжатая фотография'),
        ),
    ]
