"""
PRACTICAL SOLUTION: Prettier Budget Property with Currency Formatting (FLASK-H6-P12)
====================================================
ID: FLASK-H6-P12
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Implement a `prettier_budget` property on User that formats budgets of 4 or more digits with commas (e.g. 1000 -> '1,000$') and smaller budgets with a trailing '$'.

Explanation:
Implement prettier_budget using string slicing and concatenation.
"""

# Solution:
class User:
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def prettier_budget(self):
        s = str(self.budget)
        if len(s) >= 4:
            return f"{s[:-3]},{s[-3:]}$"
        else:
            return f"{s}$"

if __name__ == '__main__':
    u1 = User(1000)
    u2 = User(500)
    u3 = User(10500)
    assert hasattr(u1, 'prettier_budget')
    assert u1.prettier_budget == "1,000$"
    assert u2.prettier_budget == "500$"
    assert u3.prettier_budget == "10,500$"
    print("✓ Task 87 passed!")
