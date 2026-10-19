"""
Simulate a day
"""
import random
from event import trigger_event

def process_consequences(kingdom):
    remaining = []

    for consequence in kingdom.pending_consequences:
        if consequence["day"] > kingdom.day:
            remaining.append(consequence)

        print(f"\nConsequence of {consequence['reason']}!")

        for effect in consequence["effects"]:
            resource = effect["resource"]
            required = effect["amount"]
            available = getattr(kingdom, resource)

            shortage = max(0, required - available)
            deducted = min(required, available)

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

                kingdom.happiness = max(0, kingdom.happiness - penalty)

                print(
                    f"Insufficient {resource}! "
                    f"Short by {shortage}. "
                    f"Happiness: -{penalty}"
                )

            print(f"{resource}: -{deducted}")

    kingdom.pending_consequences = remaining


def simulate_day(kingdom):
    # Advance time
    kingdom.day += 1

    print(f"\n--- Starting day {kingdom.day} ---")

    # Resolve anything scheduled for today
    process_consequences(kingdom)

    # Trigger event
    random_trigger = random.randint(1, 4)
    if random_trigger == 1:
        trigger_event(kingdom)

    # Production
    kingdom.grain += 30
    kingdom.wood += 5
    kingdom.iron += 2

    # Consumption
    food_need = kingdom.population // 10
    kingdom.grain -= food_need


    print(f"--- End of day {kingdom.day} ---")
    return kingdom


