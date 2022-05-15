from flask import Blueprint

tasklist = Blueprint('tasklist', __name__)


@tasklist.route('/tasklist')
def tasklist():
    return '<p> Your Task List </p>'
