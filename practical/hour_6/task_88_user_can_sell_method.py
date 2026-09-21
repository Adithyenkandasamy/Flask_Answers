"""
PRACTICAL SOLUTION: User Model can_sell Ownership Verification (FLASK-H6-P13)
====================================================
ID: FLASK-H6-P13
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Implement `can_sell(self, item_obj)` on User that returns True if the item is present in `self.items`.

Explanation:
Define can_sell(self, item_obj) returning item_obj in self.items.
"""

# Solution:
class User:
    def __init__(self):
        self.items = []

    def can_sell(self, item_obj):
        return item_obj in self.items

if __name__ == '__main__':
    u = User()
    item_owned = "Item1"
    item_other = "Item2"
    u.items.append(item_owned)
    assert hasattr(u, 'can_sell'), "User must implement can_sell"
    assert u.can_sell(item_owned) is True
    assert u.can_sell(item_other) is False
    print("✓ Task 88 passed!")
