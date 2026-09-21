# FLASK-H2-T25: SQLite File-Based Nature

> **Curriculum Path:** Hour 2 Theory → Level 4: Code Interpretation  
> **Difficulty:** `Intermediate` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H2-T25`  


---

### Question
How does SQLite store database data compared to PostgreSQL or MySQL?
A) In distributed cloud memory
B) Directly inside a single ordinary file on the local filesystem
C) In browser cookies
D) In volatile RAM only

---

### 1. Direct Answer
**Correct Answer: B**

SQLite is serverless and embeds the entire database within a single local file.

### 2. In-Depth Technical Explanation
Understanding `SQLite File-Based Nature` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of SQLite File-Based Nature
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
