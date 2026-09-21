# FLASK-H6-T39: include vs extends in Jinja2

> **Curriculum Path:** Hour 6 Theory → Level 5: Comparison & Trade-offs  
> **Difficulty:** `Intermediate` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H6-T39`  


---

### Question
What is the difference between `{% include %}` and `{% extends %}` in Jinja2?

---

### 1. Direct Answer
`{% extends %}` inherits a parent layout. `{% include %}` inlines another template snippet into the current file at that exact position.

### 2. In-Depth Technical Explanation
Understanding `include vs extends in Jinja2` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of include vs extends in Jinja2
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
