# Generated by Django 3.0.1 on 2020-02-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svadebnaya_fotosessiya', '0005_auto_20200215_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='image_low',
            field=models.ImageField(default=models.ImageField(upload_to='svadebnaya_fotosessiya/albums', verbose_name='Фотография'), upload_to='svadebnaya_fotosessiya/albums/low', verbose_name='Сжатая фотография'),
        ),
    ]
