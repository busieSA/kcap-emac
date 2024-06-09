from flask import render_template, flash, redirect, url_for
from . import education
from app.nerd.nerd import *

@education.route('/')
def home():
    title = "Main Page"
    year = get_time_year()
    return render_template('education/home.html', title=title, year=year)









