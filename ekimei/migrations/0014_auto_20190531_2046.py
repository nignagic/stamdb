# Generated by Django 2.0.13 on 2019-05-31 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0013_auto_20190513_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(blank=True, max_length=200, verbose_name='アルバム名'),
        ),
        migrations.AddField(
            model_name='song',
            name='composer',
            field=models.CharField(blank=True, max_length=200, verbose_name='作曲者'),
        ),
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='説明文'),
        ),
        migrations.AddField(
            model_name='song',
            name='lyrist',
            field=models.CharField(blank=True, max_length=200, verbose_name='作詞者'),
        ),
        migrations.AddField(
            model_name='song',
            name='namerb',
            field=models.CharField(blank=True, max_length=200, verbose_name='曲名カナ'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=200, verbose_name='曲名'),
        ),
    ]
