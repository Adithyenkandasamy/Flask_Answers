"""
PRACTICAL SOLUTION: View Function URL Generation with url_for (FLASK-H2-P01)
====================================================
ID: FLASK-H2-P01
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Use Flask's `url_for` function to dynamically generate the URL endpoint for the `market_page` view function.

Explanation:
Pass the view function name 'market_page' as a string to url_for(), not the URL path.
"""

# Solution:
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/store/items")
def market_page():
    return "Market Items"

def get_market_url():
    with app.test_request_context():
        return url_for('market_page')

if __name__ == '__main__':
    url = get_market_url()
    assert url == "/store/items"
    print("✓ Task 16 passed!")
