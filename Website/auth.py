from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/Chatbot')
def login():
    return render_template("Chatbot.html", text="Chat Logs")


@auth.route('/TaskList')
def open_tasklist():
    return render_template("TL_base.html")


@auth.route('/Journal')
def open_journals():
    return render_template("Journal.html")


@auth.route('/Sign-up')
def sign_up():
    return render_template("Sign-up.html")
