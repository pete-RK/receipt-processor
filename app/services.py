import re
import math
from datetime import datetime
from app.models import Receipt

# Cache for storing id
cache = {}

def calculate_points(receipt: Receipt) -> int:
    points = 0
    points += len(re.findall(r'[a-zA-Z0-9]', receipt.retailer))
    total = float(receipt.total)
    
    if total.is_integer():
        points += 50
    if total % 0.25 == 0:
        points += 25
    points += (len(receipt.items) // 2) * 5
    
    # Iterate through items
    for item in receipt.items:
        trimmed_desc = item.shortDescription.strip()
        if len(trimmed_desc) % 3 == 0:
            item_price = float(item.price)
            points += math.ceil(item_price * 0.2)
    
    # Purchase date points
    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    if purchase_date.day % 2 == 1:
        points += 6

    # Purchase Time points
    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points