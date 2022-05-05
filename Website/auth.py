from flask import Blueprint

auth = Blueprint('auth', __name__)


'''this is just part of the tutorial, but it could be cool if we had like different profiles and stuff 
so I think we should keep this for now '''

@auth.route('/login')
def login():
    return "<p> Login </p>"


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"


@auth.route('/sign-up')
def sign_up():
    return "<p> Sign Up </p>"

