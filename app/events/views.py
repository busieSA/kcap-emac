from . import events
from flask import render_template, url_for
from app.events.models import BaseEvent
from app.events.forms import EventForm


@events.route('/', methods=['GET', 'POST'])
def home():
    title = "Events"
    form = EventForm()
    
    return render_template("events/home.html", title=title, form=form)
