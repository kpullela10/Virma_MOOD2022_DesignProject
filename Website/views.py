from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", salut='Welcome to Virma, your virtual medical assistant. Click one of the '
                                              'above options to proceed!')

