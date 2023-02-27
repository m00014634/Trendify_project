import requests
from flask import Flask, render_template

app = Flask(__name__)

from users import bp as users_bp
from songs import bp as songs_bp
from artists import bp as artist_bo

app.register_blueprint(users_bp)
app.register_blueprint(songs_bp)
app.register_blueprint(artist_bo)


@app.route('/')
def index():
    url = 'https://muhammadkhon.pythonanywhere.com/artists/artist'
    response = requests.get(url)
    print(response.json()['message'])
    artists = response.json()['message']

    return render_template('index.html', artists=artists)


@app.route('/<string:artist_nickname>')
def exact_artist(artist_nickname):
    url = f'https://muhammadkhon.pythonanywhere.com/artists/{artist_nickname}'
    response = requests.get(url)
    print(response.json())
    artist = response.json()

    return render_template('exact_artist.html', artist=artist)
