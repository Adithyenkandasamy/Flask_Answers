# FLASK-H1-T42: Templates Folder Name

> **Curriculum Path:** Hour 1 Theory → Level 6: Output & Status Prediction  
> **Difficulty:** `Advanced` | **Format:** `Single-Word`  
> **Question ID:** `FLASK-H1-T42`  


---

### Question
What is the exact name of the directory where Flask looks for HTML template files by default?

---

### 1. Direct Answer
`templates`

### 2. In-Depth Technical Explanation
Understanding `Templates Folder Name` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Templates Folder Name
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
