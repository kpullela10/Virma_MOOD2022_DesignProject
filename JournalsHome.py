from flask import Blueprint

journalsHome = Blueprint('journalsHome', __name__)


@journalsHome.route('/journals')
def new_journal():
    return "<p> Create a New Journal </p>"


@journalsHome.route('/previous_journal')
def previous_journals():
    return "<p> </p>"




