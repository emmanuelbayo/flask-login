from flask import Flask
from app.blueprints.auth import auth_bp

def register_blueprints(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/')