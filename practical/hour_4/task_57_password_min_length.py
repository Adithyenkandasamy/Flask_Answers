"""
PRACTICAL SOLUTION: Password Minimum Length Enforcement (FLASK-H4-P12)
====================================================
ID: FLASK-H4-P12
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Configure `password` in `RegisterForm` with `Length(min=6)` to enforce a minimum password length of 6 characters.

Explanation:
Add Length(min=6) to the password field validators.
"""

# Solution:
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    password = PasswordField('Password', validators=[Length(min=6)])

if __name__ == '__main__':
    with app.test_request_context():
        form = RegisterForm()
        len_val = [v for v in form.password.validators if isinstance(v, Length)]
        assert len(len_val) > 0
        assert len_val[0].min == 6
        print("✓ Task 57 passed!")

