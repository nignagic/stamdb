# Generated by Django 2.0.13 on 2019-05-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0006_movie_reg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='niconico_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='youtube_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
