import requests
from flask import Blueprint, request, render_template, redirect

bp = Blueprint('artist', __name__, url_prefix='/artist')


@bp.route('/registration', methods=['POST', 'GET'])
def register_artist():
    if request.method == 'POST':
        artist_name = request.form['artist_name']

        response = requests.post(f'https://muhammadkhon.pythonanywhere.com/artists/artist?nickname={artist_name}')

        return redirect('/')

    else:
        return render_template('registration/artist_reg.html')
