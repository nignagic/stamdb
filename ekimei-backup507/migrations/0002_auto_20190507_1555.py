# Generated by Django 2.0.13 on 2019-05-07 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='line',
        ),
        migrations.DeleteModel(
            name='Line',
        ),
    ]
