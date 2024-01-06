from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
import bcrypt
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        #users = db.users
        #logged_user = users.find_one({'username' : name})
        try:
            logged_user = User.objects.get(username=name)
        except:
            flash('Invalid username & password combination.', category='error')
            return render_template("login.html", user=current_user)

        if logged_user:
            if bcrypt.hashpw(password.encode('utf-8'), logged_user.password.encode('utf-8')) == logged_user.password.encode('utf-8'):
                flash('Logged in Successfully!', category='success')
                login_user(logged_user, remember=True)
                return redirect(url_for('views.timer'))
            else:
                flash('Invalid username & password combination.', category='error')
        else:
            flash('Invalid username & password combination.', category='error')


    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

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
                login_user(new_user, remember=True)
                flash('Account created!', category='success')

                return redirect(url_for('views.timer'))
            else:
                flash('Username already exists.', category='error')

    return render_template("register.html")