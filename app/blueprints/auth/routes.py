from app.blueprints.auth import auth_bp

from flask import render_template

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    title = "Login Page"
    return render_template('auth/login.html', title=title)