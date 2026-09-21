"""
PRACTICAL SOLUTION: Custom Form Validator Method Naming (FLASK-H4-P07)
====================================================
ID: FLASK-H4-P07
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Implement a custom validator method on `RegisterForm` named `validate_username` that checks whether a username already exists.

Explanation:
WTForms automatically invokes custom validators following the naming convention validate_<field_name>.
"""

# Solution:
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    username = StringField('Username')

    def validate_username(self, field):
        if field.data == "admin":
            raise ValidationError("Username taken")

if __name__ == '__main__':
    assert hasattr(RegisterForm, 'validate_username'), "Validator method must be named validate_username"
    print("✓ Task 52 passed!")
