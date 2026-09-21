"""
PRACTICAL SOLUTION: Package Execution Guard in Entry Point (FLASK-H3-P02)
====================================================
ID: FLASK-H3-P02
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
In the root `run.py` entry point, verify that `app.run()` only executes when the script is run directly as `__main__`.

Explanation:
Check module_name == '__main__' to ensure server only runs when executed directly.
"""

# Solution:
def should_run_server(module_name: str) -> bool:
    return module_name == '__main__'

if __name__ == '__main__':
    assert should_run_server('__main__') is True
    assert should_run_server('market') is False
    print("✓ Task 32 passed!")
