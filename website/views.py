from flask import Blueprint, render_template, request
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    # print(current_user.logoutPage)
    current_user.logoutPage = request.url
    # print(current_user.logoutPage)
    db.session.commit()
    return render_template("home.html", user=current_user)

@views.route('/blackandwhite')
@login_required
def blackandwhite():
    # print(current_user.logoutPage)
    current_user.logoutPage = request.url
    # print(current_user.logoutPage)
    db.session.commit()
    return render_template("blackandwhite.html", user=current_user)

@views.route('/blueandyellow')
@login_required
def blueandyellow():
    # print(current_user.logoutPage)
    current_user.logoutPage = request.url
    # print(current_user.logoutPage)
    db.session.commit()
    return render_template("blueandyellow.html", user=current_user)