# Backend/auth/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from models.user_model import db, User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from auth.email_utils import send_reset_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return redirect(url_for("auth.signup"))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("Signup successful! Please log in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("signup.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)  # ✅ This logs in the user
            flash("Login successful!", "success")
            return redirect(url_for("main_routes.search"))  # ✅ Redirects to /chat

        flash("Invalid credentials.", "error")
    return render_template("login.html")



@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You’ve been logged out.", "info")
    return redirect(url_for("auth.login"))

@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()

        # ✅ Even if user doesn't exist, show the same message
        if user:
            send_reset_email(user)

        # ✅ Don't reveal whether the email was valid or not
        flash("If your email is registered, you will receive a reset link.", "info")
        return redirect(url_for("auth.login"))

    return render_template("forgot_password.html")


@auth_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
    s = URLSafeTimedSerializer("your-secret-key")

    try:
        email = s.loads(token, max_age=3600)
    except (SignatureExpired, BadSignature):
        flash("Reset link expired or invalid.", "error")
        return redirect(url_for("auth.login"))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash("Invalid user.", "error")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        password = request.form["password"]
        user.set_password(password)
        db.session.commit()
        flash("Password reset successful!", "success")
        return redirect(url_for("auth.login"))

    return render_template("reset_password.html")
