"""
PRACTICAL SOLUTION: Automatic Login After User Registration (FLASK-H5-P14)
====================================================
ID: FLASK-H5-P14
Curriculum Tier: Integration | Difficulty: Advanced
Task:
After inserting a new user record in the registration route, call `login_user(user)` so the user is immediately authenticated.

Explanation:
Call login_user(user) right after saving the user to the database.
"""

# Solution:
from flask import Flask
from flask_login import LoginManager, login_user, current_user, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, uid, username):
        self.id = uid
        self.username = username

def register_and_authenticate(user: User):
    login_user(user)

if __name__ == '__main__':
    with app.test_request_context():
        u = User(10, "new_user")
        register_and_authenticate(u)
        assert current_user.is_authenticated is True
        assert current_user.username == "new_user"
    print("✓ Task 74 passed!")
