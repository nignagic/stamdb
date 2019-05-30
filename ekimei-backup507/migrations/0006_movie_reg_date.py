# Generated by Django 2.0.13 on 2019-05-07 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0005_stationinmovie_line_cd'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='reg_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date registered'),
            preserve_default=False,
        ),
    ]