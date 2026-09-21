"""
PRACTICAL SOLUTION: Deleting Database Records with Session Workflow (FLASK-H2-P15)
====================================================
ID: FLASK-H2-P15
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Implement `delete_item_by_id` to look up an item by ID, delete it from the session, and commit the change.

Explanation:
Call db.session.delete(item) followed by db.session.commit().
"""

# Solution:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))

def delete_item(item: Item):
    db.session.delete(item)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        item = Item(name="Temp")
        db.session.add(item)
        db.session.commit()
        item_id = item.id
        delete_item(item)
        assert Item.query.filter_by(id=item_id).first() is None
    print("✓ Task 30 passed!")
