"""
PRACTICAL SOLUTION: Package Architecture and Circular Import Prevention (FLASK-H3-P01)
====================================================
ID: FLASK-H3-P01
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Design the package loader so that the Flask application instance is initialized before routes are registered.

Explanation:
Instantiate the Flask app before importing and registering routes to prevent circular imports.
"""

# Solution:
from flask import Flask

class PackageInit:
    def __init__(self):
        self.app = None
        self.routes_loaded = False

    def initialize(self):
        if self.app is None:
            raise RuntimeError("Routes imported before app initialization!")
        self.routes_loaded = True

    def run_setup(self):
        self.app = Flask(__name__)
        self.initialize()

if __name__ == '__main__':
    pkg = PackageInit()
    pkg.run_setup()
    assert pkg.app is not None
    assert pkg.routes_loaded is True
    print("✓ Task 31 passed!")
