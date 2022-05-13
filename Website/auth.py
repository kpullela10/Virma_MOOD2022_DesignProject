from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


'''this is just part of the tutorial, but it could be cool if we had like different profiles and stuff 
so I think we should keep this for now '''

@auth.route('/Chatbot')
def Chatbot():
    return render_template("Chatbot.html")


@auth.route('/TaskList')
def logout():
    return render_template("TaskList.html")


@auth.route('/Journal')
def sign_up():
    return render_template("Journal.html")

