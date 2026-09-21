"""
PRACTICAL SOLUTION: Iterating Form Validation Error Messages (FLASK-H4-P09)
====================================================
ID: FLASK-H4-P09
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Extract all validation error messages from `form.errors` into a flat list of strings for display.

Explanation:
Iterate over errors.values() and unpack individual error message strings.
"""

# Solution:
errors_dict = {
    "username": ["Username is required.", "Username too short."],
    "password": ["Password is required."]
}

def extract_all_errors(errors: dict) -> list:
    out = []
    for err_list in errors.values():
        for err in err_list:
            out.append(err)
    return out

if __name__ == '__main__':
    res = extract_all_errors(errors_dict)
    assert "Username is required." in res
    assert "Username too short." in res
    assert "Password is required." in res
    print("✓ Task 54 passed!")
