"""
PRACTICAL SOLUTION: User Logout Workflow with Flash Notification (FLASK-H5-P13)
====================================================
ID: FLASK-H5-P13
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Implement a `/logout` view function that calls `logout_user()`, flashes an `'info'` message, and redirects to `home_page`.

Explanation:
Call logout_user(), flash message with category='info', and return redirect(url_for('home_page')).
"""

# Solution:
from flask import Flask, flash, redirect, url_for
from flask_login import LoginManager, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return None


@app.route('/home')
def home_page():
    return "Home"

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))

def test_logout():
    with app.test_client() as client:
        res = client.get('/logout')
        assert res.status_code == 302
        assert res.headers['Location'].endswith('/home')

if __name__ == '__main__':
    test_logout()
    print("✓ Task 73 passed!")
