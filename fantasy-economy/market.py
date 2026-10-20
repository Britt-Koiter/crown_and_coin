"""
supply and demand and prices
"""

import random

MARKETS = {
    5: {
        "name": "Royal Market",
        "prices": {
            "grain": (2, 4),
            "wood": (4, 6),
            "iron": (6, 8),
        },
    },
    12: {
        "name": "Farmers' Market",
        "prices": {
            "grain": (2, 8),
            "wood": (5, 12),
            "iron": (10, 15),
        },
    },
    15: {
        "name": "Artisan & Craft Market",
        "prices": {
            "grain": (3, 5),
            "wood": (5, 7),
            "iron": (7, 9),
        },
    },
    23: {
        "name": "Grand Trade Fair",
        "prices": {
            "grain": (3, 6),
            "wood": (3, 8),
            "iron": (5, 12),
        },
    },
    27: {
        "name": "Royal Treasury Exchange",
        "prices": {
            "grain": (4, 7),
            "wood": (6, 10),
            "iron": (8, 14),
        },
    },
}

def trigger_market(kingdom):
    market = MARKETS.get(kingdom.day)

    if market is None:
        return None

    prices = {
        resource: random.randint(*price_range)
        for resource, price_range in market["prices"].items()
    }

    print(f"\n=== {market['name']} ===")

    for resource, price in prices.items():
        print(f"{resource.title()}: {price} coins per unit")

    return {
        "day": kingdom.day,
        "name": market["name"],
        "prices": prices,
    }