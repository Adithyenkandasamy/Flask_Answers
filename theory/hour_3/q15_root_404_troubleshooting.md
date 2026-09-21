# FLASK-H3-T15: Root 404 Troubleshooting

> **Curriculum Path:** Hour 3 Theory → Level 2: Understanding  
> **Difficulty:** `Beginner` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H3-T15`  


---

### Question
If running `python run.py` serves 404 for all routes, what import step was omitted?

---

### 1. Direct Answer
`from market import routes` was omitted from `market/__init__.py`.

### 2. In-Depth Technical Explanation
Understanding `Root 404 Troubleshooting` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Root 404 Troubleshooting
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
