from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user,
                           salut='Welcome to Virma, your virtual medical assistant. We\'re here to help. Welcome to Virma, your virtual medical assistant. Click one of the '
                                 'options above to proceed!',
                           quotes='Here are some of our favorite words of encouragement:',
                           inspiration='Sometimes, life will kick you around, but sooner or later, you realize you’re not just a survivor. You’re a warrior, and you’re stronger than anything life throws your way. -Brooke Davis',
                           inspiration2='Give yourself another day, another chance. You will find your courage eventually. Don’t give up on yourself just yet. -unknown'
                           )
