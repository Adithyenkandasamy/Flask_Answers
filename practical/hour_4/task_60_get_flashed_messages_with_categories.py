"""
PRACTICAL SOLUTION: Dismissible Alert Rendering with Flash Categories (FLASK-H4-P15)
====================================================
ID: FLASK-H4-P15
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Implement `render_flash_alerts` to unpack flashed messages into a list of HTML alert elements with appropriate Bootstrap CSS classes (`alert-success`, `alert-danger`).

Explanation:
Unpack tuple (category, message) and format class attribute as alert-{category}.
"""

# Solution:
def render_flash_alerts(messages_with_cats: list) -> list:
    out = []
    for category, message in messages_with_cats:
        out.append(f"<div class='alert alert-{category}'>{message}</div>")
    return out

if __name__ == '__main__':
    flashed = [("success", "Item bought!"), ("danger", "Not enough budget!")]
    res = render_flash_alerts(flashed)
    assert "<div class='alert alert-success'>Item bought!</div>" in res
    assert "<div class='alert alert-danger'>Not enough budget!</div>" in res
    print("✓ Task 60 passed!")
