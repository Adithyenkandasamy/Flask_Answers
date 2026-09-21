# FLASK-H3-T18: debug=True in app.run

> **Curriculum Path:** Hour 3 Theory → Level 3: Mechanism  
> **Difficulty:** `Intermediate` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H3-T18`  


---

### Question
What is the effect of passing `debug=True` to `app.run()` in `run.py`?
A) Automatically commits database transactions
B) Enables auto-reloading and interactive in-browser debugger
C) Disables all routes
D) Prints SQL queries to console only

---

### 1. Direct Answer
**Correct Answer: B**

It enables debug mode directly without needing `FLASK_DEBUG=1` in the terminal.

### 2. In-Depth Technical Explanation
Understanding `debug=True in app.run` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of debug=True in app.run
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
