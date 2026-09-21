"""
PRACTICAL SOLUTION: Password Verification with check_password_hash (FLASK-H5-P05)
====================================================
ID: FLASK-H5-P05
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Implement `verify_password` to check a candidate plaintext password against the stored Bcrypt hash using `bcrypt.check_password_hash`.

Explanation:
Use bcrypt.check_password_hash(stored_hash, attempted) to securely verify passwords.
"""

# Solution:
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

def verify_password(stored_hash: str, attempted: str) -> bool:
    return bcrypt.check_password_hash(stored_hash, attempted)

if __name__ == '__main__':
    h = bcrypt.generate_password_hash("mypassword").decode('utf-8')
    assert verify_password(h, "mypassword") is True
    assert verify_password(h, "wrong") is False
    print("✓ Task 65 passed!")
