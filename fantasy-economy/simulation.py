"""
Simulate a day
"""
import random
from event import trigger_event
from market import trigger_market
from database import save_event, save_consequence, save_market, save_daily_snapshot, save_transaction

def simulate_day(con, kingdom):
    # Advance time
    kingdom.day += 1

    print(f"\n--- Starting day {kingdom.day} ---")

    # Resolve anything scheduled for today
    consequences = process_consequences(kingdom)
    save_daily_snapshot(con, kingdom)
    save_consequence(con, kingdom, consequences)

    # Trigger event
    random_trigger = random.randint(1, 4)

    if random_trigger == 1:
        event, description = trigger_event(kingdom)
        save_event(con, kingdom, event, description)
        save_daily_snapshot(con, kingdom)

    market = trigger_market(kingdom)

    if market is not None:
        save_market(con, market)

        trade(
            con,
            kingdom,
            market,
            action="buy",
            resource="wood",
            quantity=10,
        )
        save_daily_snapshot(con, kingdom)
        pass

    # Production
    kingdom.grain += 30
    kingdom.wood += 5
    kingdom.iron += 2

    # Consumption
    food_need = kingdom.population // 10
    kingdom.grain -= food_need

    print(f"--- End of day {kingdom.day} ---")
    return kingdom


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


def trade(con, kingdom, market, action, resource, quantity):
    if action not in ("buy", "sell"):
        raise ValueError("Action must be 'buy' or 'sell'")

    if resource not in market["prices"]:
        raise ValueError(f"Unknown resource: {resource}")

    if quantity <= 0:
        raise ValueError(f"Quantity is negative: {quantity}")

    price = market["prices"][resource]
    total_price = price * quantity
    stock = getattr(kingdom, resource)

    if action == "buy":
        if kingdom.treasury < total_price:
            return False

        kingdom.treasury -= total_price
        setattr(kingdom, resource, stock + quantity)

    else: # Sell
        if stock < quantity:
            return False

        kingdom.treasury += total_price
        setattr(kingdom, resource, stock - quantity)

    # Record the successful transaction
    transaction = {
        "action": action,
        "resource": resource,
        "quantity": quantity,
        "price": price,
        "total_price": total_price,
    }

    save_transaction(con, market, transaction)

    print(f"{action.title()} {quantity} {resource}"
          f" for {total_price} coins")
    return True
