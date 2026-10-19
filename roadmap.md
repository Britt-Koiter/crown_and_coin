# Crown & Coin

*A fantasy kingdom economy simulator built with Python, DuckDB and Streamlit.*

## Overview

Crown & Coin is a small interactive simulation in which the player manages a struggling fantasy kingdom.

The player controls taxation, trade and economic investments while responding to random world events such as poor harvests, resource shortages and merchant arrivals.

The goal is to maintain a prosperous and stable kingdom over a 30-day campaign.

The project combines game mechanics, data engineering, SQL analytics and interactive application development.

## Research Question

**How do taxation, resource scarcity and trade affect the economic stability of a small fantasy kingdom over time?**

### Questions to investigate

- How does the tax rate affect treasury growth and population happiness?
- How do harvest failures influence grain prices and food security?
- Can trade prevent shortages without exhausting the treasury?
- Which policy combination produces the most stable kingdom?

## Tech Stack

- **Python:** Simulation engine and game rules
- **DuckDB:** Persistent analytical database
- **Streamlit:** Interactive browser-based interface
- **Pandas:** Data handling and query results
- **Plotly:** Interactive historical charts
- **Pytest:** Unit and integration tests

## Initial Scope

The first version will contain:

- One kingdom
- One 30-day campaign
- Three resources: grain, wood and iron
- A treasury, population and happiness score
- Resource production and consumption
- Supply-and-demand-based market prices
- Taxation and basic trading
- Random economic events
- Persistent campaign history in DuckDB
- An interactive Streamlit interface
- Historical charts and SQL-based analysis

## Simulation Rules

Each in-game day follows this sequence:

1. Apply the player's selected policies.
2. Generate the day's world event, if any.
3. Produce resources.
4. Consume resources based on population needs.
5. Calculate taxes and trade expenses.
6. Update resource prices based on supply and demand.
7. Update population happiness and food security.
8. Record the resulting state, prices, transactions and events in DuckDB.
9. Check whether the kingdom has reached a failure condition.

The exact formulas will be tuned during development.

## Data Model

### `kingdom_state`

Stores one daily snapshot of the kingdom.

- `day`
- `treasury`
- `population`
- `happiness`
- `food_stock`
- `tax_rate`

### `market_history`

Stores the daily market state for each resource.

- `day`
- `resource`
- `price`
- `supply`
- `demand`

### `transactions`

Records resource purchases and sales.

- `day`
- `resource`
- `quantity`
- `unit_price`
- `total_value`
- `trade_type`

### `world_events`

Records events that affect the economy.

- `day`
- `event_type`
- `description`
- `severity`

## Project Structure

```text
crown-and-coin/
├── app.py
├── pyproject.toml
├── README.md
├── src/
│   └── crown_coin/
│       ├── __init__.py
│       ├── simulation.py
│       ├── economy.py
│       ├── database.py
│       └── analytics.py
├── sql/
│   ├── schema.sql
│   └── reports.sql
├── tests/
│   ├── test_simulation.py
│   ├── test_economy.py
│   └── test_database.py
├── data/
│   └── .gitkeep
└── .gitignore
```

The DuckDB database file will be created locally and excluded from version control.

## Weekend Roadmap

### Phase 1 — Build the Economy

- [ ] Define the kingdom's initial state.
- [ ] Define resources and starting prices.
- [ ] Implement resource production and consumption.
- [ ] Implement taxes and market prices.
- [ ] Add random world events.
- [ ] Run a 30-day simulation from the command line.

### Phase 2 — Add DuckDB

- [ ] Create the database connection.
- [ ] Create the four database tables.
- [ ] Persist daily snapshots and market history.
- [ ] Record transactions and world events.
- [ ] Write SQL queries for average prices and treasury trends.
- [ ] Verify that campaign history survives an application restart.

### Phase 3 — Build the Interface

- [ ] Display treasury, population, food stocks and happiness.
- [ ] Add controls for taxation and trading.
- [ ] Add an advance-day button.
- [ ] Display current market prices.
- [ ] Plot historical prices and treasury balance.
- [ ] Display the event log.

### Phase 4 — Test and Investigate

- [ ] Test that resource stocks cannot become negative.
- [ ] Test that purchases cannot exceed available funds.
- [ ] Test that one day is recorded only once.
- [ ] Run a high-tax and a low-tax experiment.
- [ ] Compare treasury, food security and happiness.
- [ ] Document one finding and the model's limitations.

## Future Extensions

- Multiple settlements connected by trade routes
- Different biomes and resource specializations
- Seasonal harvests and droughts
- Policy presets and campaign comparisons
- Saving and loading multiple kingdoms
- Exporting analytical tables to Parquet
- A more elaborate fantasy-themed interface

## Success Criteria

The weekend MVP is complete when:

1. A player can advance a campaign through the interface.
2. The economy changes according to implemented rules.
3. The kingdom's history is stored persistently in DuckDB.
4. Historical SQL queries produce meaningful results.
5. At least one policy experiment can be compared and explained.

## Limitations

The simulation uses fictional data and simplified economic rules. Its results describe the behaviour of this model, not real-world economies.

The initial version is a local, single-player prototype. Multiplayer, complex pathfinding and large-scale world generation are out of scope.
