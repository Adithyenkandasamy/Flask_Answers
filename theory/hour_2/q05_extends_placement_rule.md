# FLASK-H2-T05: extends Placement Rule

> **Curriculum Path:** Hour 2 Theory → Level 1: Definition  
> **Difficulty:** `Beginner` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H2-T05`  


---

### Question
Where must the `{% extends %}` tag be placed in a child template?
A) Inside the `<body>` tag
B) Anywhere in the file
C) As the very first line/tag of the template
D) At the very bottom

---

### 1. Direct Answer
**Correct Answer: C**

It must be the first line of the child template; any markup before or outside blocks will be ignored or raise an error.

### 2. In-Depth Technical Explanation
Understanding `extends Placement Rule` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of extends Placement Rule
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
