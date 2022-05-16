from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", salut='Welcome to Virma, your virtual medical assistant. Click one of the '
                                              'options above to proceed!',quotes='Here are some of our favorite words of encouragement:', inspiration='Sometimes, life will kick you around, but sooner or later, you realize you’re not just a survivor. You’re a warrior, and you’re stronger than anything life throws your way. -Brooke Davis',
                                              inspiration2='Give yourself another day, another chance. You will find your courage eventually. Don’t give up on yourself just yet. -unknown', inspiration3='There is hope, even when your brain tells you there isn’t. -John Green', inspiration4='And if today all you did was hold yourself together, I’m proud of you. -unknown')

