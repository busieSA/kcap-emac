from flask import render_template
from . import rules

@rules.route('/')
def terms():
    return "hello terms"


