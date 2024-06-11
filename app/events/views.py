from . import events
from flask import render_template, url_for
from app.events.forms import EventForm


@events.route('/', methods=['GET', 'POST'])
def home():
    title = "Events"
    form = EventForm()
    #query the db for events to list on the site here    
    return render_template("events/home.html", title=title, form=form)


@events.route('/create-event', methods=['POST'])
def create_event():
    title = "Create New Event"
    form = EventForm()
    return render_template('', title=title, form=form)


@events.route('/update-event')
def update_event():
    return "update event here"

@events.route('/delete-event')
def delete_event():
    return "Delete event Here"

