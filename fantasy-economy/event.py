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
    {
        "name": "Harvest Festival",
        "type": "festival",
        "weight": 20,
    },
    {
        "name": "Miner's Luck",
        "type": "resource",
        "weight": 25
    },
    {
        "name": "Crop Blight",
        "type": "agriculture",
        "weight": 25
    }
]


def trigger_event(kingdom):
    # Get a random event
    event = random.choices(
        EVENTS,
        weights=[e["weight"] for e in EVENTS],
        k=1,
    )[0]

    description = ""

    if event["name"] == "Storm":
        print(
            f"day: {kingdom.day}"
            "\nA terrible storm is coming!"
            "\n🪵 The storm damages the kingdom's wood supply! 🪵"
        )
        wood_lost = random.randint(15, 30)
        kingdom.wood = max(0, kingdom.wood - wood_lost)
        description = f"A storm is damaging the kingdom. lost {wood_lost} wood"
        kingdom.pending_consequences.append({
            "day": kingdom.day + 1,
            "reason": "Storm",
            "effects": [
                {"resource": "treasury", "amount": random.randint(20, 40),},
                {"resource": "wood", "amount": 10},
            ],
        })

        print(f"Wood lost: {wood_lost}")
        print("Repairs will be needed tomorrow!")

    elif event["name"] == "Harvest Festival":
        print(
            f"day: {kingdom.day}"
            "\nThe harvest festival is coming!🌾"
        )
        income = random.randint(20, 40)
        kingdom.treasury += income
        happiness = random.randint(5, 15)
        kingdom.happiness += happiness
        population_increase = random.randint(1,12)
        kingdom.population += population_increase

        description = (
            f"The harvest festival raised {income} coins, "
            f"increased happiness by {happiness}, "
            f"and attracted {population_increase} people."
        )
        print(f"income: +{income}")
        print(f"Happiness: +{happiness}")

    elif event["name"] == "Miner's Luck":
        print(
            f"day: {kingdom.day}"
            "\nThere is miners luck on our side today!"
        )
        iron_increase = random.randint(20, 50)
        kingdom.iron += iron_increase
        print(f"iron: +{iron_increase}")
        description = f"Miners discovered an extra {iron_increase} iron."

    elif event["name"] == "Crop Blight":
        print(
            f"day: {kingdom.day}"
            "\nDiseases are ruining the crops"
        )
        resource = "grain"
        required = random.randint(20, 50)
        available = getattr(kingdom, resource)
        deducted = min(required, available)
        description = f"Diseases destroyed {deducted} grain."
        shortage = max(0, required - available)
        setattr(kingdom, resource, available - deducted)
        if shortage > 0:
            if shortage < 10:
                penalty = 2.5
            elif shortage < 15:
                penalty = 5.0
            elif shortage < 25:
                penalty = 7.5
            else:
                penalty = 15.0
            kingdom.happiness =  max(0, kingdom.happiness - penalty)
            print(
                f"Insufficient {resource}! "
                f"Short by {shortage}. "
                f"Happiness: -{penalty}"
            )
        print(f"{resource}: -{deducted}")

    return event, description