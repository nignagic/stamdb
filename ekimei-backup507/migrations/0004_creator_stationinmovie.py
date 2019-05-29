# Generated by Django 2.0.13 on 2019-05-07 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei', '0003_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StationInMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_movie', models.IntegerField()),
                ('station_name', models.CharField(max_length=200)),
                ('back_rel', models.IntegerField(default=0, verbose_name='back station relationship')),
                ('creator_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audio_creator', to='ekimei.Creator')),
                ('creator_m', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_creator', to='ekimei.Creator')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekimei.Movie')),
                ('station_cd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekimei.Station')),
            ],
        ),
    ]
