from flask import Flask, render_template



def create_app():
    '''
    Create the flask app to host the chat
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "younevergethis"

    with app.app_context():
        from .views import view
        app.register_blueprint(view,url_prefix="/")
        return app