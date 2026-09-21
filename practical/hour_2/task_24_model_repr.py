"""
PRACTICAL SOLUTION: Model String Representation with __repr__ (FLASK-H2-P09)
====================================================
ID: FLASK-H2-P09
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Implement the `__repr__` method on the `Item` model to return a readable string format `f'Item {self.name}'`.

Explanation:
Define def __repr__(self): return f'Item {self.name}' on the model class.
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

    def __repr__(self):
        return f"Item {self.name}"

if __name__ == '__main__':
    item = Item(name="Phone")
    assert repr(item) == "Item Phone"
    print("✓ Task 24 passed!")
