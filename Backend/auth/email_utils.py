# Backend/auth/email_utils.py

from flask_mail import Mail, Message
from flask import current_app
from itsdangerous import URLSafeTimedSerializer

# Define mail instance here (NOT importing from app.py)
mail = Mail()

def send_reset_email(user):
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = s.dumps(user.email)

    msg = Message("Reset Your Password",
              sender=current_app.config["MAIL_USERNAME"],
              recipients=[user.email, "admin@example.com", "dev@example.com"])

    link = f"http://localhost:5000/reset-password/{token}"
    msg.body = f"Hi {user.username},\n\nClick the link to reset your password:\n{link}\n\nThis link will expire in 1 hour."

    mail.send(msg)
