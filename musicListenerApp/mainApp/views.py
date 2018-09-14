from django.shortcuts import render
from mainApp.models import User, Playlist, Song, SongsOnPlaylist


def index(request):
    print(User.objects.all())
    # user = create_user("ivan", "123")
    # user.save()
    # playlist = create_playlist(user)
    # playlist.save()
    # song = create_song("blur-song2.mp3")
    # song.save()
    # songs_on_playlist = add_to_playlist(playlist, song)
    # songs_on_playlist.save()
    return render(request, 'mainPage.html')


def home(request):
    return render(request, 'home.html')


def create_user(name, password):
    user = User()
    user.name = name
    user.password = password
    return user


def add_to_playlist(playlist, song):
    songs_on_playlist = SongsOnPlaylist()
    songs_on_playlist.user_id = playlist.user_id
    songs_on_playlist.playlist_id = playlist.id
    songs_on_playlist.song_id = song.id
    return songs_on_playlist


def create_playlist(user):
    playlist = Playlist()
    playlist.user_id = user.id
    playlist.playlist_name = "Favourite"
    return playlist


def create_song(name):
    song = Song()
    song.name = name
    return song
