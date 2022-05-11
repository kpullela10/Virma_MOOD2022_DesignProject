from flask import Blueprint

auth = Blueprint('auth', __name__)


'''this is just part of the tutorial, but it could be cool if we had like different profiles and stuff 
so I think we should keep this for now '''

@auth.route('/Chatbot')
def login():
    return "<p> Chatbot </p>"


@auth.route('/TaskList')
def logout():
    return "<p> TaskList </p>"


@auth.route('/Journal')
def sign_up():
    return "<p> Journal </p>"

