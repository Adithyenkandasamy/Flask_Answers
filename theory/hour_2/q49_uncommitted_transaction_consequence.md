# FLASK-H2-T49: Uncommitted Transaction Consequence

> **Curriculum Path:** Hour 2 Theory → Level 7: Debugging Reasoning  
> **Difficulty:** `Advanced` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H2-T49`  


---

### Question
What happens if you call `db.session.add(item)` but the script terminates before `db.session.commit()`?
A) Data is saved automatically on exit
B) The database is deleted
C) The staged changes are discarded and nothing is written to disk
D) A SyntaxError occurs

---

### 1. Direct Answer
**Correct Answer: C**

Transactions are atomic; uncommitted changes in session memory are discarded if not explicitly committed.

### 2. In-Depth Technical Explanation
Understanding `Uncommitted Transaction Consequence` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Uncommitted Transaction Consequence
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
