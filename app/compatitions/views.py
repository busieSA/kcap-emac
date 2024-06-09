from . import compatitions
from flask import render_template, url_for


@compatitions.route('/')
def home():
    title = "Compatitions"
    return render_template("compatitions/home.html", title=title)
