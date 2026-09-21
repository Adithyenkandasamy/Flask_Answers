# FLASK-H5-T52: Conditional Navbar for Auth Users

> **Curriculum Path:** Hour 5 Theory → Level 7: Debugging Reasoning  
> **Difficulty:** `Advanced` | **Format:** `Code-Snippet`  
> **Question ID:** `FLASK-H5-T52`  


---

### Question
Show how Jinja2 checks if a user is logged in inside `base.html`.

---

### 1. Direct Answer
```jinja2
{% if current_user.is_authenticated %}
    <!-- show Logout and user info -->
{% else %}
    <!-- show Login and Register -->
{% endif %}
```

### 2. In-Depth Technical Explanation
Understanding `Conditional Navbar for Auth Users` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Conditional Navbar for Auth Users
from flask import Flask

app = Flask(__name__)

# Core implementation pattern
if __name__ == '__main__':
    # Execution entry point
    pass
```

### 4. Why This Concept Matters
Mastering this concept prevents critical runtime bugs, eliminates security vulnerabilities, and enables developers to transition seamlessly from toy scripts to production-ready Flask backends.

### 5. Common Pitfalls & Debugging Gotchas
- **Context Pitfall**: Accessing application or request variables without an active Flask context raises `RuntimeError`.
- **Naming & Scope**: Ensure variables and imports match exact casing (e.g. `Flask` class vs `flask` module).
- **Silent Failures**: Always inspect terminal traceback logs and status codes when diagnosing request handling anomalies.
