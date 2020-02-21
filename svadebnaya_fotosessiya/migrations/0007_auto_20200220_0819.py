# Generated by Django 3.0.1 on 2020-02-20 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svadebnaya_fotosessiya', '0006_foto_image_low'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='image',
            field=models.ImageField(blank=True, upload_to='svadebnaya_fotosessiya/albums', verbose_name='Фотография хорошего качества'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='image_low',
            field=models.ImageField(default=None, upload_to='svadebnaya_fotosessiya/albums/low', verbose_name='Сжатая фотография'),
        ),
    ]
