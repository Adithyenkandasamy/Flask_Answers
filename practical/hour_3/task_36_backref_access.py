"""
PRACTICAL SOLUTION: Relationship Backref Access (FLASK-H3-P06)
====================================================
ID: FLASK-H3-P06
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Access an item's owner through its `owned_user` relationship backref and return the owner's username.

Explanation:
Access item.owned_user directly without querying User table manually.
"""

# Solution:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30))
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

def get_item_owner_name(item: Item) -> str:
    return item.owned_user.username if item.owned_user else "Unknown"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User(username="alice")
        db.session.add(u)
        db.session.commit()
        item = Item(name="Camera", owner=u.id)
        db.session.add(item)
        db.session.commit()
        assert item.owned_user.username == "alice"
        assert get_item_owner_name(item) == "alice"
    print("✓ Task 36 passed!")
