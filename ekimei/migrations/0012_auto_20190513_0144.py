# Generated by Django 2.0.13 on 2019-05-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0011_auto_20190512_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationinmovie',
            name='station_nonlist_cd',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ekimei.NonListStation'),
        ),
    ]