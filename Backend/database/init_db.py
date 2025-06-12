import sys
import os
import random
from faker import Faker
from flask import Flask

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import Config
from models.product_model import db, Product
from models.user_model import User

fake = Faker()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

        categories = ['Electronics', 'Books', 'Textiles']

        for i in range(1, 101):
            product = Product(
                name=fake.catch_phrase(),
                category=random.choice(categories),
                price=round(random.uniform(10.0, 999.99), 2),
                description=fake.text(max_nb_chars=100),
                stock=random.randint(1, 100),
                image_url=f"https://picsum.photos/seed/{i}/200/200"
            )
            db.session.add(product)

        book1 = Product(
            name="Advanced Python Programming",
            category="Books",
            price=499.00,
            description="Learn Python with real-world examples. Covers Flask, APIs, and more.",
            stock=25,
            image_url="https://picsum.photos/seed/book1/200/200"
        )

        book2 = Product(
            name="Data Science Notebook",
            category="Books",
            price=299.00,
            description="Notebook with dot grid pages for data science journaling and ML workflows.",
            stock=50,
            image_url="https://picsum.photos/seed/book2/200/200"
        )

        db.session.add(book1)
        db.session.add(book2)

        db.session.commit()
        print("✅ Database initialized with 102 products (including 2 books).")

if __name__ == "__main__":
    create_app()
