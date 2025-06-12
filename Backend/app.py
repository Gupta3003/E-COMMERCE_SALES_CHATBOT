# Backend/app.py

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
from models import db  # ✅ import from models/__init__.py
from models.user_model import User
from routes.main_routes import main_routes
from auth.routes import auth_bp
from auth.email_utils import mail
from flask import redirect, url_for

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # 👇 Redirect root URL to login page
    @app.route("/")
    def home():
        return redirect(url_for('auth.login'))

    app.register_blueprint(main_routes)
    app.register_blueprint(auth_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
