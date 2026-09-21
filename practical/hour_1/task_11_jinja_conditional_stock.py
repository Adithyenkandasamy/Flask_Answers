"""
PRACTICAL SOLUTION: Jinja Conditional Rendering for Stock Status (FLASK-H1-P11)
====================================================
ID: FLASK-H1-P11
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Render a template string displaying 'In Stock' if stock > 0, otherwise 'Out of Stock'.

Explanation:
Use {% if stock > 0 %}In Stock{% else %}Out of Stock{% endif %} in the Jinja template.
"""

# Solution:
from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = "{% if stock > 0 %}In Stock{% else %}Out of Stock{% endif %}"

def render_stock(count: int) -> str:
    with app.app_context():
        return render_template_string(TEMPLATE, stock=count)

if __name__ == '__main__':
    assert render_stock(5).strip() == "In Stock"
    assert render_stock(0).strip() == "Out of Stock"
    print("✓ Task 11 passed!")
