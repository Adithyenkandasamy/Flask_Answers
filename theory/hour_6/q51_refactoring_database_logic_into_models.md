# FLASK-H6-T51: Refactoring Database Logic into Models

> **Curriculum Path:** Hour 6 Theory → Level 7: Debugging Reasoning  
> **Difficulty:** `Advanced` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H6-T51`  


---

### Question
Why is encapsulating `buy()` and `sell()` methods directly on the `Item` model good practice?

---

### 1. Direct Answer
It follows the **'Fat Models, Skinny Controllers'** architecture, keeping route handlers clean and centralizing business rules.

### 2. In-Depth Technical Explanation
Understanding `Refactoring Database Logic into Models` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Refactoring Database Logic into Models
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
