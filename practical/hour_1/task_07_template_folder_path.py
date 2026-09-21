"""
PRACTICAL SOLUTION: Custom Template Directory Configuration (FLASK-H1-P07)
====================================================
ID: FLASK-H1-P07
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Configure the Flask application instance to locate templates in a custom directory named 'my_templates'.

Explanation:
Pass template_folder='my_templates' when initializing Flask.
"""

# Solution:
from flask import Flask

app = Flask(__name__, template_folder="my_templates")

if __name__ == '__main__':
    assert app.template_folder == "my_templates"
    print("✓ Task 07 passed!")
