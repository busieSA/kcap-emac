import os
from flask import render_template, request, redirect, url_for, flash, current_app
from . import comp
from app import db
from app.comp.models import Comp
from datetime import datetime
from app.nerd.nerd import generate_unique_filename
from werkzeug.utils import secure_filename

@comp.route('/')
def home():
    # Query the database for all competitions
    title = "competitions"
    competitions = Comp.query.all()
    current_time = datetime.utcnow()
    return render_template('comp/home.html', competitions=competitions, current_time=current_time)


@comp.route('/add-competition', methods=['GET', 'POST'])
def add_competition():
    if request.method == 'POST':
        name = request.form['name']
        date_str = request.form['date']
        description = request.form['description']
        status = request.form.get('status', 'upcoming')
        location = request.form.get('location')
        max_participants = request.form.get('max_participants')

        # Handling image file here
        if 'file' not in request.files:
            flash('Ensure you have uploaded a valid image file', category='error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', category='error')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            unique_filename = generate_unique_filename(filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)  # Save the file to the specified path

        date = datetime.fromisoformat(date_str)
        new_competition = Comp(
            name=name,
            date=date,
            description=description,
            status=status,
            location=location,
            max_participants=max_participants,
            filename=unique_filename
        )
        db.session.add(new_competition)
        db.session.commit()
        flash('Competition added successfully!', 'success')
        return redirect(url_for('comp.home'))
    return render_template('comp/add_comp.html')



@comp.route('/update-competition/<int:id>', methods=['GET', 'POST'])
def update_competition(id):
    competition = Comp.query.get_or_404(id)

    if request.method == 'POST':
        name = request.form['name']
        date_str = request.form['date']
        description = request.form['description']
        status = request.form.get('status', 'upcoming')
        location = request.form.get('location')
        max_participants = request.form.get('max_participants')

        # Handling image file here
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            filename = secure_filename(file.filename)
            unique_filename = generate_unique_filename(filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)  # Save the new file to the specified path
            competition.filename = unique_filename  # Update the filename in the competition record

        # Update other competition details
        competition.name = name
        competition.date = datetime.fromisoformat(date_str)
        competition.description = description
        competition.status = status
        competition.location = location
        competition.max_participants = max_participants

        db.session.commit()
        flash('Competition updated successfully!', 'success')
        return redirect(url_for('comp.home'))

    return render_template('comp/update_comp.html', competition=competition)



@comp.route('/delete-competition/<int:id>', methods=['POST'])
def delete_competition(id):
    competition = Comp.query.get_or_404(id)
    db.session.delete(competition)
    db.session.commit()
    flash('Competition deleted successfully!', 'success')
    return redirect(url_for('comp.home'))
