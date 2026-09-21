# FLASK-H1-T36: Missing Dynamic Route Parameter

> **Curriculum Path:** Hour 1 Theory → Level 5: Comparison & Trade-offs  
> **Difficulty:** `Intermediate` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H1-T36`  


---

### Question
What error is raised if a dynamic route defines `/user/<name>` but the function is written as `def user_page():`?
A) SyntaxError
B) TypeError: user_page() takes 0 positional arguments but 1 was given
C) 404 Not Found
D) RecursionError

---

### 1. Direct Answer
**Correct Answer: B**

Flask passes captured route parameters as arguments to the view function; if the function signature does not accept them, Python raises a `TypeError`.

### 2. In-Depth Technical Explanation
Understanding `Missing Dynamic Route Parameter` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Missing Dynamic Route Parameter
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
