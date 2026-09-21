# FLASK-H2-T09: Shared Navigation Bar Placement

> **Curriculum Path:** Hour 2 Theory → Level 2: Understanding  
> **Difficulty:** `Beginner` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H2-T09`  


---

### Question
Why is the `<nav>` tag placed inside `base.html` rather than individual page templates?

---

### 1. Direct Answer
Because the navbar is shared across all pages; putting it in `base.html` ensures updates apply automatically to all inheriting pages without duplication.

### 2. In-Depth Technical Explanation
Understanding `Shared Navigation Bar Placement` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Shared Navigation Bar Placement
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
