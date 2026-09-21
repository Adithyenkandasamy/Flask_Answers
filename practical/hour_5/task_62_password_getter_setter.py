"""
PRACTICAL SOLUTION: Password Hashing Property and Setter (FLASK-H5-P02)
====================================================
ID: FLASK-H5-P02
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Implement a `@property` and `@password.setter` on the User model that generates and stores a Bcrypt password hash.

Explanation:
Decorate with @password.setter to hash passwords on assignment.
"""

# Solution:
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

class User:
    def __init__(self):
        self.password_hash = None

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text):
        self.password_hash = bcrypt.generate_password_hash(plain_text).decode('utf-8')

if __name__ == '__main__':
    u = User()
    u.password = "secret123"
    assert u.password_hash != "secret123"
    assert bcrypt.check_password_hash(u.password_hash, "secret123")
    print("✓ Task 62 passed!")
