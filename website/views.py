from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len('note') < 1:
            flash('empty note not allowed', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!!', category='success')
    return render_template("home.html", user=current_user)


@views.route('/colorBlindPage')
@login_required
def colorBlind():
    return render_template("colorBlind.html", user=current_user)