# Generated by Django 2.0.13 on 2019-05-11 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationinmovie',
            name='station_nonlist_cd',
        ),
    ]
