# FLASK-H4-T20: HTTP 405 Method Not Allowed

> **Curriculum Path:** Hour 4 Theory → Level 3: Mechanism  
> **Difficulty:** `Intermediate` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H4-T20`  


---

### Question
Why does submitting a POST form to a route configured only for GET result in HTTP 405?

---

### 1. Direct Answer
The HTTP 405 status code explicitly indicates the server recognizes the URL but refuses to accept the requested HTTP method.

### 2. In-Depth Technical Explanation
Understanding `HTTP 405 Method Not Allowed` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of HTTP 405 Method Not Allowed
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
