# Generated by Django 2.0.13 on 2019-05-12 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0012_auto_20190513_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationinmovie',
            name='station_nonlist_cd',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimei.NonListStation'),
        ),
    ]
