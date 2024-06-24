from flask import Flask, redirect, url_for, request, render_template
from . import funda
from app import db
from app.funda.models import School, Gender, Teacher, Area, Tel, Synopsis, Performer


# Define the route to handle the form
@funda.route('/create_entry', methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        # Extract data from the form
        school_name = request.form.get('school_name')
        teacher_name = request.form.get('teacher_name')
        teacher_surname = request.form.get('teacher_surname')
        teacher_email = request.form.get('teacher_email')
        tel_number = request.form.get('tel_number')
        area_name = request.form.get('area_name')
        synopsis_text = request.form.get('synopsis_text')
        performer_name = request.form.get('performer_name')
        performer_surname = request.form.get('performer_surname')
        performer_age = request.form.get('performer_age')
        gender_name = request.form.get('gender_name')

        # Create instances of each model and insert into the database
        # Assuming you handle validation and error checking as needed
        school = School(name=school_name)
        db.session.add(school)
        db.session.commit()


        # Get the ID of the newly created school
        school_id = school.id

        teacher = Teacher(name=teacher_name, surname=teacher_surname, email=teacher_email, school_id=school.id)
        db.session.add(teacher)
        db.session.commit()

        tel = Tel(number=tel_number, teacher_id=teacher.id)
        db.session.add(tel)
        db.session.commit()

        area = Area(name=area_name, school_id=school.id)
        db.session.add(area)
        db.session.commit()

        synopsis = Synopsis(text=synopsis_text, school_id=school.id)
        db.session.add(synopsis)
        db.session.commit()

        performer = Performer(name=performer_name, surname=performer_surname, age=performer_age, school_id=school.id)
        db.session.add(performer)
        db.session.commit()

        gender = Gender(name=gender_name, performer_id=performer.id)
        db.session.add(gender)
        db.session.commit()

        # Redirect to a success page or wherever needed
        return redirect(url_for('funda.success_page', school_id=school_id))

    # If GET request, render the form
    return render_template('funda/create_entry.html')


@funda.route('/add_performers/<int:id>', methods=['GET', 'POST'])
def add_performers(id):
    school = School.query.get_or_404(id)
    
    if request.method == 'POST':
        performer_names = request.form.getlist('performer_name')
        performer_surnames = request.form.getlist('performer_surname')
        performer_ages = request.form.getlist('performer_age')
        performer_genders = request.form.getlist('performer_gender')
        
        for name, surname, age, gender in zip(performer_names, performer_surnames, performer_ages, performer_genders):
            performer = Performer(name=name, surname=surname, age=age, gender=gender, school_id=id)
            db.session.add(performer)
        
        db.session.commit()
        return redirect(url_for('funda.school_details', id=id))
    
    return render_template('funda/add_performers.html', school=school)


# Define a success page route if needed
@funda.route('/success/<int:school_id>')
def success_page(school_id):
    school = School.query.get_or_404(school_id)

    return render_template('funda/success.html', school=school)


@funda.route('/school-details/<int:id>')
def school_details(id):
    school = School.query.get_or_404(id)
    performers = Performer.query.filter_by(school_id=id).all()
    area = school.area
    synopsis = school.synopsis

    return render_template('funda/school_details.html', school=school, performers=performers, area=area)



@funda.errorhandler(400)
def bad_request(e):
    return render_template("400.html", title='Bad request', year=year)

@funda.errorhandler(401)
def unauthorized(e):
    return render_template("401.html", title='Unauthorized', year=year)

@funda.errorhandler(403)
def forbidden(e):
    return render_template("403.html", title='Forbidden', year=year)

@funda.errorhandler(404)
def not_found(e):
    return render_template("404.html", title='Not found', year=year)

@funda.errorhandler(405)
def method_not_allowed():
    return render_template('405.html', title='Method not allowed', year=year)

@funda.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", title='internal-server-error', year=year)
