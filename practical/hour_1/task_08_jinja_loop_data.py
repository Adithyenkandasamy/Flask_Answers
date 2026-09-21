"""
PRACTICAL SOLUTION: Data Formatting for Jinja Loops (FLASK-H1-P08)
====================================================
ID: FLASK-H1-P08
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Format the catalog records so that each item dictionary contains 'id', 'name', 'barcode' (12 digits), and 'price' keys.

Explanation:
Extract existing code/barcode or provide a valid 12-digit default string.
"""

# Solution:
items = [
    {"id": 1, "name": "Phone", "code": "123456789012", "price": 500},
    {"id": 2, "name": "Laptop", "price": 900}
]

def format_items(raw_items):
    formatted = []
    for item in raw_items:
        barcode = item.get("code") or item.get("barcode") or "000000000000"
        formatted.append({
            "id": item["id"],
            "name": item["name"],
            "barcode": barcode,
            "price": item["price"]
        })
    return formatted

if __name__ == '__main__':
    out = format_items(items)
    for row in out:
        assert "barcode" in row
        assert len(row["barcode"]) == 12, "Barcode must be 12 digits"
    print("✓ Task 08 passed!")
