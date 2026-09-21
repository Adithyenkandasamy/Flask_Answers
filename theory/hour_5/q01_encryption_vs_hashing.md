# FLASK-H5-T01: Encryption vs Hashing

> **Curriculum Path:** Hour 5 Theory → Level 1: Definition  
> **Difficulty:** `Beginner` | **Format:** `Short-Answer`  
> **Question ID:** `FLASK-H5-T01`  


---

### Question
What is the fundamental difference between encryption and cryptographic hashing?

---

### 1. Direct Answer
**Encryption** is a two-way function (can be decrypted with a key). **Hashing** is a one-way mathematical function (cannot be reversed to plaintext).

### 2. In-Depth Technical Explanation
Understanding `Encryption vs Hashing` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Encryption vs Hashing
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
