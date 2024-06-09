from flask import render_template, flash
from app.website import website
from app.website.models import Subscriber, ContactUs, Event
from app.website.forms import SubscriberForm, ContactUsForm
from app.nerd.nerd import *

year = get_time_year()

@website.route('/')
@website.route('/home')
def home():
    title ="Home Page"
    get_id = generate_client_id()
   # flash('hello, now!!!', category='info')
    return render_template("website/home.html", title=title, get_id=get_id, year=year)


@website.route('/contact-us', methods=["POST", "GET"])
def contact_us():
    title = "Contact-Us"
    year = get_time_year()
    form= ContactUsForm()
    return render_template("website/contact-us.html", title=title, year=year, 
                           form=form)

@website.route('/subscribe', methods=['POST'])
def subscribe():
    pass

@website.route('/upcoming')
def upcoming():
    title = "Upcoming"
    events = Event.query.all()
    return render_template('website/upcoming.html', title=title, year=year, events=events)

@website.route('/donate', methods=['GET', 'POST'])
def donate():
    title = "donate-to-kcap"
    return render_template("website/donate.html", title=title)


@website.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title='page-not-found', year=year)

@website.errorhandler(500)
def internal_server_error(e):
    return render_template("404.html", title='internal-server-error', year=year)