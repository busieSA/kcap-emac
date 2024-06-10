from . import events
from flask import render_template, url_for
from app.events.forms import EventForm


@events.route('/', methods=['GET', 'POST'])
def home():
    title = "Events"
    form = EventForm()
    
    return render_template("events/home.html", title=title, form=form)


@events.route('/create-event')
def create_event():
    return "we are working on it bear with me"