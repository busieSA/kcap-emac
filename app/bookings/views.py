from . import bookings
from flask import render_template, flash, request, redirect , url_for

@bookings.route('/')
def home():
    return "book your ticket here..."

