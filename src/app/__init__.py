from flask import Flask

from app.routes import movies

def create_app():
    
    flask_app = Flask(__name__)

    flask_app.logger.info("Service starting")  # pylint: disable=no-member

    flask_app.register_blueprint(movies, url_prefix='/v1/movies')

    return flask_app
