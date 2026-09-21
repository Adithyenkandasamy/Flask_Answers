# FLASK-H1-T30: Two Benefits of Debug Mode

> **Curriculum Path:** Hour 1 Theory → Level 4: Code Interpretation  
> **Difficulty:** `Intermediate` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H1-T30`  


---

### Question
What are the two major features provided when Debug Mode is turned on?

---

### 1. Direct Answer
1. **Automatic reloader**: Automatically restarts the server when code files are edited and saved.
2. **Interactive debugger**: Displays an in-browser debugger traceback when unhandled exceptions occur.

### 2. In-Depth Technical Explanation
Understanding `Two Benefits of Debug Mode` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Two Benefits of Debug Mode
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
