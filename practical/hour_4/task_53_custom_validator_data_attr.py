"""
PRACTICAL SOLUTION: Extracting Field Data in Custom Validator (FLASK-H4-P08)
====================================================
ID: FLASK-H4-P08
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
In the custom email validator, access the entered string via `field_obj.data` to check for duplicate emails.

Explanation:
Access field_obj.data to obtain the input string from the field.
"""

# Solution:
from wtforms.validators import ValidationError

existing_emails = ["alice@market.com", "bob@market.com"]

class DummyField:
    def __init__(self, val):
        self.data = val

def validate_email_address(field_obj):
    if field_obj.data in existing_emails:
        raise ValidationError("Email already exists")

if __name__ == '__main__':
    try:
        validate_email_address(DummyField("alice@market.com"))
        assert False, "Should raise ValidationError"
    except ValidationError:
        pass
    print("✓ Task 53 passed!")
