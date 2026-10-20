"""duckdb and storage"""


def setup_database(con):
    # kingdom daily
    con.execute("""
        CREATE TABLE IF NOT EXISTS kingdom_snapshots (
            snapshot_id INTEGER PRIMARY KEY,
            day INTEGER,
            treasury INTEGER,
            population INTEGER,
            happiness FLOAT,
            grain INTEGER,
            wood INTEGER,
            iron INTEGER
        )
    """)

    # kingdom event_history
    con.execute("""
        CREATE TABLE IF NOT EXISTS event_histroy (
            day INTEGER,
            event_name VARCHAR,
            event_type VARCHAR,
            description VARCHAR
        )
    """)

    # kingdom consequence_history
    con.execute("""
        CREATE TABLE IF NOT EXISTS consequence_history (
            day INTEGER,
            resource VARCHAR,
            amount_required INTEGER,
            amount_paid INTEGER,
            shortage INTEGER)
    """)

    # kingdom markets
    con.execute("""
        CREATE TABLE IF NOT EXISTS markets (
            market_type VARCHAR,
            grain_price INTEGER,
            wood_price INTEGER,
            iron_price INTEGER,)
    """)

    # kingdom transaction_history
    con.execute("""
        CREATE TABLE IF NOT EXISTS transaction_history (
            market_type VARCHAR,
            action VARCHAR,
            resource VARCHAR,
            quantity INTEGER,
            total_price INTEGER,)
    """)


def save_daily_snapshot(con, kingdom):
    current_state = kingdom.kingdom_state()

    con.execute("""
        INSERT INTO kingdom_snapshots (
            snapshot_id, day, treasury, population, happiness,
            grain, wood, iron
        )
        SELECT COALESCE(MAX(snapshot_id), 0) + 1,
               ?, ?, ?, ?, ?, ?, ?
        FROM kingdom_snapshots
    """, [
        current_state["day"],
        current_state["treasury"],
        current_state["population"],
        current_state["happiness"],
        current_state["grain"],
        current_state["wood"],
        current_state["iron"],
    ])


def save_event(con, kingdom, event, description):
    con.execute("""
    INSERT INTO event_histroy (day, event_name, event_type, description)
        VALUES (?, ?, ?, ?)
                """, [kingdom.day, event["name"], event["type"], description])


def save_consequence(con, kingdom, consequences):
    for consequence in consequences:
        con.execute("""
                    INSERT INTO consequence_history (day, resource, amount_required, amount_paid, shortage)
                    VALUES (?, ?, ?, ?, ?)""", [kingdom.day, consequence["resource"], consequence["required"], consequence["paid"], consequence["shortage"]])


def save_market(con, market):
    con.execute("""INSERT INTO markets (market_type, grain_price, wood_price, iron_price) VALUES (?, ?, ?, ?)""", [
        market["name"], market["prices"]["grain"], market["prices"]["wood"], market["prices"]["iron"]
    ])


def save_transaction(con, market, transaction):
    con.execute("""INSERT INTO transaction_history (market_type, action, resource, quantity, total_price) VALUES (?, ?, ?, ?, ?)""", [
        market["name"], transaction["action"], transaction["resource"], transaction["quantity"], transaction["price"]
    ])