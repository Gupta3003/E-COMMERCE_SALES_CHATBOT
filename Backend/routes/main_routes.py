from flask import Blueprint, render_template, request
from flask_login import login_required
from models.product_model import Product

main_routes = Blueprint('main_routes', __name__)

@main_routes.route("/chat", methods=["GET", "POST"])
@login_required
def search():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form.get("query", "").lower()
        if query:
            results = Product.query.filter(
                Product.name.ilike(f"%{query}%") |
                Product.description.ilike(f"%{query}%") |
                Product.category.ilike(f"%{query}%")
            ).all()

    return render_template("index.html", query=query, results=results)
