from werkzeug.security import generate_password_hash
from datetime import datetime
import calendar
import uuid
### random identification generator (CLIENT ID) 

import random
import string



# identification and unique names functions

def generate_unique_filename(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    unique_filename = f'{uuid.uuid4().hex}.{ext}'
    return unique_filename

def generate_client_id():
    characters = string.ascii_letters + string.digits
    random_reff = ''.join(random.choices(characters, k=5))
    return "KCAP" + random_reff

def generate_compatition_id():
    characters = string.ascii_letters + string.digits
    random_reff = ''.join(random.choices(characters, k=7))
    return "COMP" + random_reff

def generate_event_id():
    characters = string.ascii_letters + string.digits
    random_reff = ''.join(random.choices(characters, k=8))
    return "EVENT" + random_reff


### werkzeug security here###

def generate(password):
    hp = generate_password_hash(password, method="scrypt")
    return hp

def get_time():
    now = datetime.now()
    date = now.strftime("%y-%m-%d %H:%M:%S")
    return date

def get_time_time():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

# get date allows to formate the way u want to appear
def time_check():
    now = datetime.now()
    date = now.strftime("%y-%m-%d")
    return date

def get_time_date():
    date = datetime.now().date()
    return date

def get_time_year():
    now = datetime.now()
    year = now.year
    return year

def get_time_month():
    now = datetime.now()
    month = now.month
    return month

def get_time_day():
    now = datetime.now()
    day = now.day
    return day

#def generate_client_code(name):
    '''
    generates random castomer code, 
    takes in client_name and adds it to random number as str not int
    '''



        
#cal = calendar.monthcalendar(year, month)