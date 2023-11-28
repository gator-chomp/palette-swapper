from flask import Blueprint, render_template, request
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    print(current_user.logoutPage)
    current_user.logoutPage = request.url
    print(current_user.logoutPage)
    db.session.commit()
    return render_template("home.html", user=current_user)

@views.route('/colorBlindPage')
@login_required
def colorBlind():
    print(current_user.logoutPage)
    current_user.logoutPage = request.url
    print(current_user.logoutPage)
    db.session.commit()
    return render_template("colorBlind.html", user=current_user)