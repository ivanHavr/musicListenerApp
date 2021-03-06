# Generated by Django 2.1.1 on 2018-09-14 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=20)),
                ('user_id', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 9, 14, 20, 15, 33, 517875))),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 9, 14, 20, 15, 33, 517875))),
            ],
        ),
        migrations.CreateModel(
            name='SongsOnPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('playlist_id', models.IntegerField()),
                ('song_id', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 9, 14, 20, 15, 33, 518874))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 9, 14, 20, 15, 33, 489893))),
            ],
        ),
    ]
