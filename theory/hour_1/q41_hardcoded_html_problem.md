# FLASK-H1-T41: Hardcoded HTML Problem

> **Curriculum Path:** Hour 1 Theory → Level 6: Output & Status Prediction  
> **Difficulty:** `Advanced` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H1-T41`  


---

### Question
List two reasons why returning raw HTML strings inside Python functions is bad practice.

---

### 1. Direct Answer
1. **Violates Separation of Concerns**: Mixes presentation logic with application routing.
2. **No Syntax Highlighting & Tooling**: IDEs cannot validate HTML/CSS inside Python strings, making code error-prone and hard to maintain.

### 2. In-Depth Technical Explanation
Understanding `Hardcoded HTML Problem` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Hardcoded HTML Problem
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
