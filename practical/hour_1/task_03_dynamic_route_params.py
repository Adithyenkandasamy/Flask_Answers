"""
PRACTICAL SOLUTION: Dynamic Routing with URL Arguments (FLASK-H1-P03)
====================================================
ID: FLASK-H1-P03
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Define a route '/about/<username>' that accepts a dynamic username argument in the URL and reflects it in the response.

Explanation:
Add the URL variable 'username' as a parameter to the view function signature.
"""

# Solution:
from flask import Flask

app = Flask(__name__)

@app.route("/about/<username>")
def about_page(username):
    return f"<h1>About Page of {username}</h1>"

def test_dynamic_route():
    with app.test_client() as client:
        res = client.get('/about/john')
        assert res.status_code == 200
        assert b"About Page of john" in res.data

if __name__ == '__main__':
    test_dynamic_route()
    print("✓ Task 03 passed!")
