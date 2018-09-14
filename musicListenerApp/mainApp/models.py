from django.db import models
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name + ", created: " + str(self.created)


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=20)
    user_id = models.IntegerField()
    created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.playlist_name + ",user id: " + self.user_id + ",created: " + self.created


class Song(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(default=datetime.now())


class SongsOnPlaylist(models.Model):
    user_id = models.IntegerField()
    playlist_id = models.IntegerField()
    song_id = models.IntegerField()
    created = models.DateTimeField(default=datetime.now())

