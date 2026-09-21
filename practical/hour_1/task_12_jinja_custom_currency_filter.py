"""
PRACTICAL SOLUTION: Custom Jinja Template Filter for Currency (FLASK-H1-P12)
====================================================
ID: FLASK-H1-P12
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Register a custom Jinja filter named 'currency' that appends '$' to the numeric value.

Explanation:
Register the filter with @app.template_filter('currency') on a formatting function.
"""

# Solution:
from flask import Flask, render_template_string

app = Flask(__name__)

@app.template_filter('currency')
def currency_filter(val):
    return f"{val}$"

TEMPLATE = "<p>{{ price | currency }}</p>"

def render_price(price: int) -> str:
    with app.app_context():
        return render_template_string(TEMPLATE, price=price)

if __name__ == '__main__':
    out = render_price(500)
    assert "<p>500$</p>" in out
    print("✓ Task 12 passed!")
