"""
PRACTICAL SOLUTION: Configuring HTTP Methods on Route Decorator (FLASK-H4-P02)
====================================================
ID: FLASK-H4-P02
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Update the route decorator for `/register` to allow both GET and POST HTTP request methods.

Explanation:
Add methods=['GET', 'POST'] to the @app.route decorator.
"""

# Solution:
from flask import Flask

app = Flask(__name__)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    return "Register Page"

def test_post_allowed():
    with app.test_client() as client:
        res = client.post('/register')
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"

if __name__ == '__main__':
    test_post_allowed()
    print("✓ Task 47 passed!")
