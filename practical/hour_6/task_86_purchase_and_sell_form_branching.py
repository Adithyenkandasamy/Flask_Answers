"""
PRACTICAL SOLUTION: POST Request Action Branching for Purchase vs Sell (FLASK-H6-P11)
====================================================
ID: FLASK-H6-P11
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Distinguish between purchase actions (when 'purchased_item' is in form) and sell actions (when 'sold_item' is in form).

Explanation:
Check presence of specific hidden keys in request.form to identify the modal action.
"""

# Solution:
def process_post_action(form_data: dict) -> str:
    if "purchased_item" in form_data:
        return "purchase"
    elif "sold_item" in form_data:
        return "sell"
    return "unknown"

if __name__ == '__main__':
    assert process_post_action({"purchased_item": "Phone"}) == "purchase"
    assert process_post_action({"sold_item": "Laptop"}) == "sell"
    assert process_post_action({}) == "unknown"
    print("✓ Task 86 passed!")
