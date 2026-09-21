# FLASK-H3-T53: Multiple Passwords Allowed

> **Curriculum Path:** Hour 3 Theory → Level 7: Debugging Reasoning  
> **Difficulty:** `Advanced` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H3-T53`  


---

### Question
Why does `password_hash` NOT have `unique=True`?
A) Passwords cannot be checked for uniqueness
B) Two different users can legitimately choose the same password
C) SQLite does not support unique on strings
D) Bcrypt hashes are always identical

---

### 1. Direct Answer
**Correct Answer: B**

Multiple users can choose identical passwords; with salting, their generated hashes are different anyway.

### 2. In-Depth Technical Explanation
Understanding `Multiple Passwords Allowed` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Multiple Passwords Allowed
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
