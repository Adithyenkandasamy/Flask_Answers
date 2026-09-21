"""
PRACTICAL SOLUTION: HiddenField for Modal Form Submissions (FLASK-H4-P14)
====================================================
ID: FLASK-H4-P14
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Define a `PurchaseItemForm` with a `SubmitField` and a `HiddenField` named `purchased_item`.

Explanation:
Declare purchased_item = HiddenField('Purchased Item') on the form.
"""

# Solution:
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class PurchaseItemForm(FlaskForm):
    purchased_item = HiddenField('Purchased Item')
    submit = SubmitField('Purchase')

if __name__ == '__main__':
    from wtforms import HiddenField
    with app.test_request_context():
        form = PurchaseItemForm()
        assert hasattr(form, 'purchased_item'), "Form must define purchased_item field"
        assert isinstance(form.purchased_item, HiddenField)
    print("✓ Task 59 passed!")
