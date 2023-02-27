import requests
from flask import Blueprint, request, render_template, redirect

bp = Blueprint('songs', __name__, url_prefix='/songs')


@bp.route('/')
def get_all_songs():
    url = 'https://muhammadkhon.pythonanywhere.com/songs/song'
    response = requests.get(url)
    print(response.json())
    songs = response.json()

    return render_template('songs.html', songs=songs)


@bp.route('/<string:song_name>')
def exact_song(song_name):
    url = f'https://muhammadkhon.pythonanywhere.com/songs/{song_name}'
    response = requests.get(url)
    print(response.json())
    song = response.json()

    return render_template('exact_song.html', song=song)
