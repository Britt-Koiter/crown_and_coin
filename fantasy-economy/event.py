"""
Events
"""

import random

EVENTS = [
    {
        "name": "Storm",
        "type": "weather",
        "weight": 15,
    },
    # Add other events once their effects are implemented.
]


def trigger_event(kingdom):
    # Get a random event
    event = random.choices(
        EVENTS,
        weights=[e["weight"] for e in EVENTS],
        k=1,
    )[0]

    if event["name"] == "Storm":
        print(
            f"day: {kingdom.day}"
            "\nA terrible storm is coming!"
            "\n🪵 The storm damages the kingdom's wood supply! 🪵"
        )

        wood_lost = random.randint(15, 30)
        kingdom.wood = max(0, kingdom.wood - wood_lost)

        kingdom.pending_consequences.append({
            "day": kingdom.day + 1,
            "reason": "Storm",
            "effects": [
                {
                    "resource": "treasury",
                    "amount": random.randint(20, 40),
                },
                {
                    "resource": "wood",
                    "amount": 10,
                },
            ],
        })

        print(f"Wood lost: {wood_lost}")
        print("Repairs will be needed tomorrow!")

    return event