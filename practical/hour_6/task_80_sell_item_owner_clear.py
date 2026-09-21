"""
PRACTICAL SOLUTION: Clearing Item Ownership on Sale (FLASK-H6-P05)
====================================================
ID: FLASK-H6-P05
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
When an item is sold back to the market, set its `owner` attribute to `None`.

Explanation:
Set item.owner = None to release item back to the market.
"""

# Solution:
class Item:
    def __init__(self, owner_id):
        self.owner = owner_id

def release_item_to_market(item: Item):
    item.owner = None

if __name__ == '__main__':
    item = Item(owner_id=5)
    release_item_to_market(item)
    assert item.owner is None
    print("✓ Task 80 passed!")
