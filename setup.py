"""
Initialzing the database and kingdom
"""

kingdom_state = {
    "day": 0,
    "treasury": 0,
    "population": 0,
    "happiness": 0,
    "grain": 0,
    "wood": 0,
    "iron": 0
}

start_state = {
    "population": 100,
    "treasury": 500,
    "grain": 300,
    "wood": 100,
    "iron": 500
}


market_history = {
    "day": 0,
    "resource": 0,
    "price": 0,
    "supply": 0,
    "demand": 0
}

transactions = {
    "day": 0,
    "resource": 0,
    "quantity": 0,
    "unit_price": 0,
    "total_value": 0,
    "trade_type": 0
}

world_events = {
    "day": 0,
    "event_type": "",
    "description": "",
    "severity": "",
}