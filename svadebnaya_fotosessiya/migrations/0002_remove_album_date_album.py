# Generated by Django 3.0.1 on 2020-01-07 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('svadebnaya_fotosessiya', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='date_album',
        ),
    ]