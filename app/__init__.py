from flask import Flask
from app.blueprints import register_blueprints
import os

def create_app():
    app = Flask(__name__, 
                static_folder=os.path.join(os.path.dirname(__file__), 'views/static'),
                template_folder=os.path.join(os.path.dirname(__file__), 'views/templates')
                )
    register_blueprints(app)

    return app