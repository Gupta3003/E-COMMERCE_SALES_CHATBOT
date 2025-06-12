# backend/utils/query_handler.py

from models.product_model import Product

def search_products(query):
    query = query.lower()
    return Product.query.filter(
        Product.name.ilike(f"%{query}%") |
        Product.description.ilike(f"%{query}%") |
        Product.category.ilike(f"%{query}%")
    ).all()

