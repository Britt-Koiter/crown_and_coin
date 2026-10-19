"""
Data generator
"""

resources_overview = {
    "grain": {"price": 4, "daily_production": 100},
    "wood": {"price": 6, "daily_production": 40},
    "iron": {"price": 12, "daily_production": 15},
}

start_state = {
    "population": 100,
    "treasury": 500,
    "grain": 300,
    "wood": 100,
    "iron": 500
}

kingdom_state = {
    "day": 0,
    "treasury": 0,
    "population": 0,
    "happiness": 0,
    "grain": 0,
    "wood": 0,
    "iron": 0
}