from . import comp


@comp.route('/')
def home():
    return "welcome to the applications' compatitions add page here"


@comp.route('/add-compatition', methods=['GET', 'POST'])
def add_compatition():
    return "ADD new event"

@comp.route('/update-compatition', methods=['GET', 'POST'])
def update_compatition():
    return "Update event page here"

#not sure about delet event here

@comp.route('/delete-compatition', methods=['GET', 'POST'])
def delete_compatition():
    return "Delete Event here"




