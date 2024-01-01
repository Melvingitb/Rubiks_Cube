from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('name')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(password) < 2:
            flash('Password must be greater than 2 characters.', category='error')
        elif password != confirm:
            flash('Passwords do not match.', category='error')
        else:
            # add to database
            flash('Account created!', category='success')
    return render_template("register.html")