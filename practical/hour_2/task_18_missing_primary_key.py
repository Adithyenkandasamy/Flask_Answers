"""
PRACTICAL SOLUTION: Primary Key Definition on SQLAlchemy Model (FLASK-H2-P03)
====================================================
ID: FLASK-H2-P03
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Define the `Item` model schema with an integer primary key column named `id`.

Explanation:
Every SQLAlchemy model table requires at least one primary_key=True column.
"""

# Solution:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        assert hasattr(Item, 'id')
        assert Item.id.primary_key is True
        print("✓ Task 18 passed!")
