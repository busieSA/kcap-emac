from flask import render_template, url_for, redirect, flash
from . import admin
from app.nerd.nerd import get_time_year


@admin.route('/', methods=['GET', 'POST'])
def home():
    title = "Admin User Login"
    return render_template('admin/login.html', title=title)


@admin.route('/register', methods=["GET", "POST"])
def register():
    title = "Register-Admin_User"
    return render_template('admin/register.html', title=title)


@admin.route('/dashboard')
def dashboard():
    return render_template('admin/NiceAdmin/index.html', year=get_time_year())