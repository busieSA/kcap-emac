from . import admin
from flask import render_template, url_for, redirect, flash

@admin.route('/', methods=['GET', 'POST'])
def home():
    title = "Admin User Login"
    return render_template('admin/login.html', title=title)


@admin.route('/register', methods=["GET", "POST"])
def register():
    title = "Register-Admin_User"
    return render_template('admin/register.html', title=title)


