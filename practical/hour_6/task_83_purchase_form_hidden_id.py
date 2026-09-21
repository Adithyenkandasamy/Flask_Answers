"""
PRACTICAL SOLUTION: Extracting Form Field Data from Submission (FLASK-H6-P08)
====================================================
ID: FLASK-H6-P08
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Extract the integer item ID from the submitted purchase form data dictionary.

Explanation:
Cast int(form_dict.get('purchased_item', 0)).
"""

# Solution:
def extract_item_id(form_dict: dict) -> int:
    return int(form_dict.get('purchased_item', 0))

if __name__ == '__main__':
    data = {"purchased_item": "42"}
    assert extract_item_id(data) == 42
    print("✓ Task 83 passed!")
