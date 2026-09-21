"""
PRACTICAL SOLUTION: Enforcing Unique Constraints on User Email (FLASK-H3-P13)
====================================================
ID: FLASK-H3-P13
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Attempting to insert a user with a duplicate email address must raise an exception and be caught safely.

Explanation:
Catch the integrity error and roll back the session when duplicate emails violate unique constraints.
"""

# Solution:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)

def create_user_email(email_str: str) -> bool:
    with app.app_context():
        db.create_all()
        try:
            u = User(email=email_str)
            db.session.add(u)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

if __name__ == '__main__':
    assert create_user_email("user@test.com") is True
    assert create_user_email("user@test.com") is False
    print("✓ Task 43 passed!")
