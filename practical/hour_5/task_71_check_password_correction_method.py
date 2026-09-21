"""
PRACTICAL SOLUTION: User check_password_correction Method Implementation (FLASK-H5-P11)
====================================================
ID: FLASK-H5-P11
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Implement a `check_password_correction(attempted_password)` method on User that checks against `self.password_hash`.

Explanation:
Define check_password_correction(self, attempted_password) calling bcrypt.check_password_hash.
"""

# Solution:
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

class User:
    def __init__(self, pwd):
        self.password_hash = bcrypt.generate_password_hash(pwd).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

if __name__ == '__main__':
    u = User("mypass123")
    assert hasattr(u, 'check_password_correction'), "User must implement check_password_correction"
    assert u.check_password_correction("mypass123") is True
    assert u.check_password_correction("wrong") is False
    print("✓ Task 71 passed!")
