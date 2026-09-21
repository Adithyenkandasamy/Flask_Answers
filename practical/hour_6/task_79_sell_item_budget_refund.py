"""
PRACTICAL SOLUTION: Refunding User Budget on Item Sale (FLASK-H6-P04)
====================================================
ID: FLASK-H6-P04
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Implement `sell_item` to refund the sold item's price back to the selling user's budget.

Explanation:
Increment user budget with user.budget += price.
"""

# Solution:
class User:
    def __init__(self, budget: int):
        self.budget = budget

def refund_sale(user: User, price: int) -> int:
    user.budget += price
    return user.budget

if __name__ == '__main__':
    u = User(500)
    refund_sale(u, 200)
    assert u.budget == 700
    print("✓ Task 79 passed!")
