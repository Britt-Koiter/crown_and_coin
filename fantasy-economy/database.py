"""duckdb and storage"""


def setup_database(con):
    # kingdom daily
    con.execute("""
        CREATE TABLE IF NOT EXISTS kingdom_daily (
            day INTEGER PRIMARY KEY,
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

def save_daily_snapshot(con, kingdom):
   current_state = kingdom.kingdom_state()
   con.execute("""
               INSERT INTO kingdom_daily (day, treasury, population, happiness,
                                          grain, wood, iron)
               VALUES (?, ?, ?, ?, ?, ?, ?)
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