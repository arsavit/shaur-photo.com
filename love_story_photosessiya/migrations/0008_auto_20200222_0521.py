# Generated by Django 3.0.1 on 2020-02-22 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('love_story_photosessiya', '0007_auto_20200222_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foto_love',
            options={'ordering': ('pk',), 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
