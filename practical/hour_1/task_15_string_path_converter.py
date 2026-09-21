"""
PRACTICAL SOLUTION: Path Route Converter for Multi-Segment URLs (FLASK-H1-P15)
====================================================
ID: FLASK-H1-P15
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Configure a route '/files/<path:filepath>' to match multiple path segments including slashes.

Explanation:
Use <path:filepath> in the route definition to capture slashes within the argument.
"""

# Solution:
from flask import Flask

app = Flask(__name__)

@app.route("/files/<path:filepath>")
def get_file(filepath):
    return f"Path: {filepath}"

def test_path():
    with app.test_client() as client:
        res = client.get('/files/docs/readme.txt')
        assert res.status_code == 200
        assert b"Path: docs/readme.txt" in res.data

if __name__ == '__main__':
    test_path()
    print("✓ Task 15 passed!")
