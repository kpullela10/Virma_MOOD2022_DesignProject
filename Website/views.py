from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", salut = "Welcome to Virma, your virtual therapist! Click an option to proceed")
