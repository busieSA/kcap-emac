import os 
import uuid 
from . import gallery
from app import db
from flask import render_template, flash,  redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
from app.nerd.nerd import generate_unique_filename
from app.gallery.models import Media
from flask_login import current_user, login_required
#from app.gallery.forms import 





@gallery.route('/')
def home():
    title = "Images Gallery Page"
    images = Media.query.all()
    return render_template('gallery/home.html', title=title, images=images)

@gallery.route('/upload', methods=['POST', 'GET'])
@login_required
def upload_images():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('please select a valid file', category='error')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            unique_filename = generate_unique_filename(filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
            print(f"Saving file to {filepath}")  # Debugging line
            file.save(filepath)
            new_image = Media(filename = unique_filename)
            db.session.add(new_image)
            db.session.commit()
            flash('Image Upload successful', category='success')
            return redirect(url_for('gallery.home'))        
    return render_template('gallery/upload.html')