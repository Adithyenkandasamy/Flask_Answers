# FLASK-H1-T02: Django vs Flask

> **Curriculum Path:** Hour 1 Theory → Level 1: Definition  
> **Difficulty:** `Beginner` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H1-T02`  


---

### Question
Which of the following components is included natively in Django but NOT in Flask core?
A) URL routing
B) Built-in Object Relational Mapper (ORM)
C) HTTP request handling
D) HTML templating

---

### 1. Direct Answer
**Correct Answer: B) Built-in Object Relational Mapper (ORM)**

Flask does not include an ORM out of the box; developers integrate libraries such as Flask-SQLAlchemy.

### 2. In-Depth Technical Explanation
Understanding `Django vs Flask` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Django vs Flask
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
