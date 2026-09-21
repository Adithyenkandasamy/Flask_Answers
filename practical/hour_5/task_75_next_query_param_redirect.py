"""
PRACTICAL SOLUTION: Next Parameter Redirection After Login (FLASK-H5-P15)
====================================================
ID: FLASK-H5-P15
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Extract the `next` query parameter from `request.args` to redirect users back to their requested protected page, or default to `market_page`.

Explanation:
Use request_args.get('next') and fallback to default route if None.
"""

# Solution:
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/market')
def market_page(): return "Market"

@app.route('/items')
def items_page(): return "Items"

def get_redirect_target(request_args: dict) -> str:
    next_page = request_args.get('next')
    return next_page if next_page else "/market"

if __name__ == '__main__':
    assert get_redirect_target({"next": "/items"}) == "/items"
    assert get_redirect_target({}) == "/market"
    print("✓ Task 75 passed!")
