"""
PRACTICAL SOLUTION: Validating Ownership Before Item Sale (FLASK-H6-P09)
====================================================
ID: FLASK-H6-P09
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Validate that an item belongs to the current user before processing a sale request.

Explanation:
Verify item.owner == current_user_id before initiating transaction.
"""

# Solution:
class Item:
    def __init__(self, owner_id):
        self.owner = owner_id

def validate_can_sell(item: Item, current_user_id: int) -> bool:
    return item.owner == current_user_id

if __name__ == '__main__':
    item1 = Item(owner_id=5)
    assert validate_can_sell(item1, 5) is True, "Owner 5 should be permitted to sell item"
    assert validate_can_sell(item1, 9) is False, "User 9 should NOT be permitted to sell user 5's item"
    print("✓ Task 84 passed!")
