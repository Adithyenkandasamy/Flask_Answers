# FLASK-H2-T14: Invalid Endpoint in url_for

> **Curriculum Path:** Hour 2 Theory → Level 2: Understanding  
> **Difficulty:** `Beginner` | **Format:** `Single-Word`  
> **Question ID:** `FLASK-H2-T14`  


---

### Question
What exception does Flask raise if `url_for()` is called with a non-existent view function name?

---

### 1. Direct Answer
`BuildError` (or `werkzeug.routing.BuildError`)

### 2. In-Depth Technical Explanation
Understanding `Invalid Endpoint in url_for` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Invalid Endpoint in url_for
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
