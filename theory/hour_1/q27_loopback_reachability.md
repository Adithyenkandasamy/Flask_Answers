# FLASK-H1-T27: Loopback Reachability

> **Curriculum Path:** Hour 1 Theory → Level 4: Code Interpretation  
> **Difficulty:** `Intermediate` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H1-T27`  


---

### Question
Can another computer on your home Wi-Fi network view your website via `http://127.0.0.1:5000`?
A) Yes, because 127.0.0.1 is a public IP
B) No, 127.0.0.1 only loops back internally inside the local host machine
C) Only if they know the admin password
D) Yes, if port forwarding is enabled on the router

---

### 1. Direct Answer
**Correct Answer: B**

127.0.0.1 is strictly the internal loopback interface of the local host.

### 2. In-Depth Technical Explanation
Understanding `Loopback Reachability` is central to Flask web development. Flask follows a modular WSGI architecture where view functions, decorators, and extensions work in concert. Adhering to Python conventions ensures clean separation of concerns, robust request dispatching, and secure application lifecycle management.

### 3. Practical Code Example
```python
# Practical demonstration of Loopback Reachability
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
