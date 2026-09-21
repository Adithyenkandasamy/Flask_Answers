"""
PRACTICAL SOLUTION: Custom HTTP Status Codes (FLASK-H1-P04)
====================================================
ID: FLASK-H1-P04
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Configure the item endpoint to return a 404 status code with message 'Item not found' when an unrecognized item name is requested.

Explanation:
Return a tuple ('Item not found', 404) to return the 404 HTTP status code.
"""

# Solution:
from flask import Flask

app = Flask(__name__)

@app.route("/item/<name>")
def item_page(name):
    if name != "phone":
        return "Item not found", 404
    return "Found item", 200

def test_status_code():
    with app.test_client() as client:
        res = client.get('/item/laptop')
        assert res.status_code == 404
        assert b"not found" in res.data

if __name__ == '__main__':
    test_status_code()
    print("✓ Task 04 passed!")
