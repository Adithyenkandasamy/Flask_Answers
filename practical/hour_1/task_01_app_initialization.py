"""
PRACTICAL SOLUTION: Flask Application Initialization (FLASK-H1-P01)
====================================================
ID: FLASK-H1-P01
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Initialize a Flask application instance properly so that it exports an `app` object with a valid configuration and module name.

Explanation:
Import Flask with capital 'F' from flask and pass __name__ to the Flask() constructor.
"""

# Solution:
from flask import Flask

app = Flask(__name__)

def get_app():
    return app

if __name__ == '__main__':
    assert get_app() is not None, "App should be initialized"
    assert get_app().import_name is not None
    print("✓ Task 01 passed!")
