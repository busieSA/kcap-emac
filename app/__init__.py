import os 
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "database.db"


def app_starter():
    app = Flask(__name__)
    load_dotenv()
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = 'app/static/imgs/uploads/'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
    app.config['SQLALCHEMY_DATABASE_URI']  = f'sqlite:///{DB_NAME}'
    app.config['ALLOWED_EXTENSIONS'] = {'npg', 'jpg', 'jpeg', 'gif'}
    



    db.init_app(app)
    migrate.init_app(app, db)
    
    #ensures Upload folder exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    #from app.funda.models import School, Gender, Teacher, Area, Tel, Synopsis, Performer
    #from app.events.models import Event, AnnualEvent
    #from app.gallery.models import Media
    from app.auth.models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    from app.auth import auth, views
    from app.website import website, views
    from app.education import education, views
    from app.events import events, views
    from app.bookings import bookings, views
    from app.gallery import gallery, views
    from app.comp import comp, views
    from app.admin import admin, views
    from app.funda import funda, views




    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(website, url_prefix='/')
    app.register_blueprint(education, url_prefix='/education')
    app.register_blueprint(events, url_prefix='/events')
    app.register_blueprint(bookings, url_prefix='/bookings')
    app.register_blueprint(gallery, url_prefix='/gallery')
    app.register_blueprint(comp, url_prefix='/compatitions')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(funda, url_prefix='/funda')


    with app.app_context():
        if not os.path.exists(app.instance_path + f'/{DB_NAME}'):
            db.create_all()
            print('Created app db')

    return app 