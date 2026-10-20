"""
Simulate a day
"""
import random
from event import trigger_event
from database import save_event, save_consequence

def process_consequences(kingdom):
    remaining = []
    resolved_consequences = []

    for consequence in kingdom.pending_consequences:
        if consequence["day"] > kingdom.day:
            remaining.append(consequence)
            continue

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
            resolved_consequences.append({
                "reason": consequence["reason"],
                "resource": resource,
                "required": required,
                "paid": deducted,
                "shortage": shortage,
            })
    kingdom.pending_consequences = remaining

    return resolved_consequences

def simulate_day(con, kingdom):
    # Advance time
    kingdom.day += 1

    print(f"\n--- Starting day {kingdom.day} ---")

    # Resolve anything scheduled for today
    consequences = process_consequences(kingdom)
    save_consequence(con, kingdom, consequences)

    # Trigger event
    random_trigger = random.randint(1, 4)

    if random_trigger == 1:
        event, description = trigger_event(kingdom)
        save_event(con, kingdom, event, description)

    # Production
    kingdom.grain += 30
    kingdom.wood += 5
    kingdom.iron += 2

    # Consumption
    food_need = kingdom.population // 10
    kingdom.grain -= food_need

    print(f"--- End of day {kingdom.day} ---")
    return kingdom


