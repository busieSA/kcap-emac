from flask import render_template, flash, request, redirect, url_for, jsonify
from app import db
from sqlalchemy import func
from app.auth import auth
from app.auth.forms import RegisterUserForm, UserLoginForm
from app.auth.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from app.nerd.nerd import *
from app.website.models import Enquiry
from app.gallery.models import Media
from collections import defaultdict



@auth.route('/')
def got_to_login():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = "User Login Page"
    form = UserLoginForm()
    
    if form.validate_on_submit() and request.method == "POST":
        email = form.email.data  # Use form data directly
        user = User.query.filter_by(email=email).first()
        
        if user:
            password = form.password.data  # Use form data directly
            password_hash = user.password_hash
            
            if check_password_hash(password_hash, password):
                login_user(user)
                flash('You are logged in!', category='success')
                return redirect(url_for('auth.user_admin'))
            else:
                flash('Invalid credentials, please try again.', category='error')
        else:
            flash('Invalid credentials, please try again.', category='error')
    
    return render_template('auth/login.html', title=title, form=form)


@auth.route('/register-user', methods=['GET', 'POST'])
def register():
    title="Register User Page"
    form = RegisterUserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            password = request.form.get('password')
            confirm = request.form.get('confirm')
            ci = generate_client_id()
            check_ci = User.query.filter_by(client_identification=ci).first()
            if check_ci is None:
                print(ci)
                client_identification = ci
            else:
                print('Hm client identification is a problem for now')
            if password != confirm:
                flash('password must match...',category='error')
            else:
                password_hash = generate_password_hash(password)
                new_user= User(
                    name = form.name.data, surname=form.surname.data,
                    client_identification=client_identification,
                    email = form.email.data, password_hash=password_hash,
                    accept_tos = form.accept_tos.data
                )

                name = form.name.data
                form.name.data = ''
                form.surname.data = ''
                form.accept_tos.data = ''

                db.session.add(new_user)
                db.session.commit() 
                flash(f'welcome {name}, your registration has been successful', category='success')
                return redirect(url_for('auth.user_admin'))
        else:
            flash('User with that email already exist', category='error')
            return render_template('auth/register.html', title=title, form=form)
    else:
        return render_template('auth/register.html', title=title, form=form)





@auth.route('/admin')
def user_admin():
    title = "temp admin"
    enquries_count = Enquiry.query.count()
    user_count = User.query.count()
    media_count = Media.query.count()

    media_uploads = db.session.query(Media.data_uploaded).all()
    date_counts = defaultdict(int)
    for record in media_uploads:
        date_str = record.data_uploaded.strftime('%Y-%m-%d')
        date_counts[date_str] += 1

    labels = list(date_counts.keys())
    print(labels)
    data = list(date_counts.values())
    print(data)

    return render_template('auth/admin.html', title=title, user=current_user,
                           enquries_count=enquries_count,
                           user_count=user_count, media_count=media_count, 
                           labels=labels, data=data)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out Successfuly', category='success')
    return redirect(url_for('auth.login'))



@auth.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title='page-not-found')

@auth.errorhandler(500)
def internal_server_error(e):
    return render_template("404.html", title='internal-server-error')
