# Generated by Django 2.1 on 2019-11-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0002_auto_20191112_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='song',
            field=models.ManyToManyField(blank=True, to='ekimei.Song', verbose_name='使用楽曲'),
        ),
        migrations.AddField(
            model_name='movie',
            name='vocal',
            field=models.ManyToManyField(blank=True, to='ekimei.Vocal', verbose_name='使用ボーカル'),
        ),
    ]
