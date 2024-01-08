from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import User, Solve
import json

# blueprints allow you to organize routes into groups
views = Blueprint('views', __name__)

# Renders home.html when a get request is sent to the base route
# Passes in the current user so the server can use it in the frontend
@views.route('/')
def home():
    return render_template("home.html", user=current_user)

# Renders timer.html when a get request is sent to the timer route
# Passes in the current user so the server can use it in the frontend
@views.route('/timer')
@login_required
def timer():
    return render_template("timer.html", user=current_user)

@views.route('/solves', methods=['GET', 'POST'])
@login_required
def solves():
    if request.method == 'POST':
        # load the JSON from the request
        solve = json.loads(request.data)
        time = float(solve['time'])
        scramble = solve['scramble']
        new_solve = Solve(time=time, scramble=scramble, user=current_user)
        new_solve.save()

        return jsonify({})


    return render_template("solves.html", user=current_user)