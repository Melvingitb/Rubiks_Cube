from flask import Blueprint, render_template, request, jsonify, flash
from flask_login import login_required, current_user
from .models import User, Solve
from . import db
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

@views.route('/solves', methods=['GET', 'POST', 'DELETE'])
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
    elif request.method== 'DELETE':
        solve = json.loads(request.data)
        id = solve['id']
        try:
            solve_delete = Solve.objects.get(pk=id)
        except:
            flash('Error deleting solve.', category='error')
            return jsonify({})
        
        solve_delete.delete()
        return jsonify({})


    user_solves = Solve.objects.order_by('-date')(user=current_user)

    return render_template("solves.html", user=current_user, solves=user_solves)