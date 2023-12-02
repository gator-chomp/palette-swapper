from flask import Blueprint, render_template, request
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
#login required to access this page
@login_required
def home():
    #allows for user to end up on home page when they log in if they log out on home page
    current_user.logoutPage = request.url
    db.session.commit()
    return render_template("home.html", user=current_user)

@views.route('/blackandwhite')
#login required to access this page
@login_required
def blackandwhite():
    #allows for user to end up on black and white page when they log in if they log out on home page
    current_user.logoutPage = request.url
    
    db.session.commit()
    return render_template("blackandwhite.html", user=current_user)

@views.route('/blueandyellow')
#login required to access this page
@login_required
def blueandyellow():
    #allows for user to end up on blue and yellow page when they log in if they log out on home page
    current_user.logoutPage = request.url
    db.session.commit()
    return render_template("blueandyellow.html", user=current_user)