"""
Start the simulation
"""
import duckdb

from kingdom import Kingdom
from simulation import simulate_day
from database import setup_database, save_daily_snapshot

con = duckdb.connect("fantasy-economy/kingdom.duckdb")

try:
    setup_database(con)
    kingdom = Kingdom()
    save_daily_snapshot(con, kingdom)
    while kingdom.day < 30:
        simulate_day(con, kingdom)
        save_daily_snapshot(con, kingdom)
        print(kingdom)
finally:
    con.close()