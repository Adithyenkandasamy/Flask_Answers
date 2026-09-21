# FLASK-H4-T19: Default Route Methods

> **Curriculum Path:** Hour 4 Theory → Level 3: Mechanism  
> **Difficulty:** `Intermediate` | **Format:** `Single-Word`  
> **Question ID:** `FLASK-H4-T19`  


---

### Question
What HTTP method is allowed by default if `methods` is omitted from `@app.route`?

---

### 1. Direct Answer
`GET`

### 2. In-Depth Technical Explanation
Understanding `Default Route Methods` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Default Route Methods
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
