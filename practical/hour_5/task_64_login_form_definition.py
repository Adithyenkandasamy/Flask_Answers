"""
PRACTICAL SOLUTION: User Login Form Definition (FLASK-H5-P04)
====================================================
ID: FLASK-H5-P04
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Create a `LoginForm` class with `username`, `password`, and `submit` fields, each with required field validators.

Explanation:
Define password = PasswordField('Password', validators=[DataRequired()]).
"""

# Solution:
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

if __name__ == '__main__':
    with app.test_request_context():
        from wtforms import PasswordField
        form = LoginForm()
        assert hasattr(form, 'password'), "LoginForm must contain a password field"
        assert isinstance(form.password, PasswordField)
        print("✓ Task 64 passed!")

