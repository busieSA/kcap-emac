from flask import render_template, flash, request, redirect, url_for
from app.website import website
from app.website.models import Subscriber, Enquiry
from app.website.forms import SubscriberForm, ContactUsForm
from app.nerd.nerd import *
from app.gallery.models import Media
from app.events.models import Event, AnnualEvent


year = get_time_year()

@website.route('/')
@website.route('/home')
def home():
    title ="Home Page"
    get_id = generate_client_id()
    images = Media.query.order_by(Media.data_uploaded.desc()).limit(6).all()
   # flash('hello, now!!!', category='info')
    return render_template("website/home.html", title=title, get_id=get_id, year=year, images=images)

@website.route('/contact-us', methods=["POST", "GET"])
def contact_us():
    title = "Contact-Us"
    year = get_time_year()
    form = ContactUsForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')  # Corrected the typo from 'subejct' to 'subject'
        message = request.form.get('message')
        
        # Process the form data (e.g., send email, save to database, etc.)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('website.contact_us'))
    
    return render_template('website/contact-us.html', title=title, year=year, form=form)


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


@website.errorhandler(400)
def bad_request(e):
    return render_template("400.html", title='Bad request', year=year)

@website.errorhandler(401)
def unauthorized(e):
    return render_template("401.html", title='Unauthorized', year=year)

@website.errorhandler(403)
def forbidden(e):
    return render_template("403.html", title='Forbidden', year=year)

@website.errorhandler(404)
def not_found(e):
    return render_template("404.html", title='Not found', year=year)

@website.errorhandler(405)
def method_not_allowed():
    return render_template('405.html', title='Method not allowed', year=year)

@website.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", title='internal-server-error', year=year)