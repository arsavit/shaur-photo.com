# Generated by Django 3.0.1 on 2020-02-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love_story_photosessiya', '0004_foto_love_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto_love',
            name='width',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ширина'),
        ),
    ]