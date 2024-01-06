from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        users = db.users
        login_user = users.find_one({'username' : name})

        if login_user:
            if bcrypt.hashpw(password.encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                flash('Logged in Successfully!', category='success')
            else:
                flash('Invalid username & password combination.', category='error')
        else:
            flash('Invalid username & password combination.', category='error')


    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if len(name) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(password) < 2:
            flash('Password must be greater than 2 characters.', category='error')
        elif password != confirm:
            flash('Passwords do not match.', category='error')
        else:
            # add to database
            users = db.users
            existing_user = users.find_one({'username' : name})

            if existing_user is None:

                new_user = User(username=name, password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
                new_user.save()
                flash('Account created!', category='success')

                return redirect(url_for('views.home'))
            else:
                flash('Username already exists.', category='error')

    return render_template("register.html")