# FLASK-H2-T26: SQLite Database File Extension

> **Curriculum Path:** Hour 2 Theory → Level 4: Code Interpretation  
> **Difficulty:** `Intermediate` | **Format:** `Single-Word`  
> **Question ID:** `FLASK-H2-T26`  


---

### Question
What common file extension was used for the database file in the tutorial?

---

### 1. Direct Answer
`.db` (e.g. `market.db`)

### 2. In-Depth Technical Explanation
Understanding `SQLite Database File Extension` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of SQLite Database File Extension
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
