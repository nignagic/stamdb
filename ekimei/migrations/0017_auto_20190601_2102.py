# Generated by Django 2.0.13 on 2019-06-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0016_auto_20190601_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocal',
            name='name',
            field=models.CharField(max_length=200, verbose_name='歌手名'),
        ),
    ]
