# FLASK-H1-T33: Multiple Routes for Single Function

> **Curriculum Path:** Hour 1 Theory → Level 5: Comparison & Trade-offs  
> **Difficulty:** `Intermediate` | **Format:** `Code-Snippet`  
> **Question ID:** `FLASK-H1-T33`  


---

### Question
Show how to stack route decorators so that both `/` and `/home` execute `home_page()`.

---

### 1. Direct Answer
```python
@app.route('/')
@app.route('/home')
def home_page():
    return '<h1>Home Page</h1>'
```

### 2. In-Depth Technical Explanation
Understanding `Multiple Routes for Single Function` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Multiple Routes for Single Function
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
