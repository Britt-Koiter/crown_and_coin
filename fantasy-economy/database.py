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
            id INTEGER PRIMARY KEY,
            day INTEGER,
            event_type VARCHAR,
            description VARCHAR
        )
    """)

    # kingdom consequence_history
    con.execute("""
        CREATE TABLE IF NOT EXISTS consequence_history (
            id INTEGER PRIMARY KEY,
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
