import requests
from flask import Blueprint, request, render_template, redirect

bp = Blueprint('users', __name__, url_prefix='/user')


@bp.route('/registration', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        password = request.form['password']  # Пока нету в апи

        result = requests.post(f'https://muhammadkhon.pythonanywhere.com/users/user?first_name={first_name}&last_name={last_name}&username={username}&password={password}&phone_number={phone_number}')

        return redirect('/')

    else:
        return render_template('registration/reg.html')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']

        response = requests.get(f'https://muhammadkhon.pythonanywhere.com/users/{username}')
        result = response.json()
        print(result)

    except:
        return render_template('registration/login.html')
