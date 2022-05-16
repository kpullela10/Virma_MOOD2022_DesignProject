from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hi Mr Sea'

    from .views import views
    from .auth import auth
    from .TaskList_App import TaskList

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
