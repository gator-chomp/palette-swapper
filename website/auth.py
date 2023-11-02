from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password1):
                flash('Logged in success!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect!!', category='error')
        else:
            flash('not a user', category='error')
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('user already exists', category='error')
        elif len(email) < 5:
            flash('Email must be atleast 5 characters', category='error')
        elif len(firstName) < 2:
            flash('first name must be atleast 2 characters', category='error')
        elif password1 != password2:
            flash('passwords do not match', category='error')
        elif len(password1) < 8:
            flash('password must be atleast 8 characters', category='error')
        else:
            new_user = User(email=email,firstName=firstName,password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)