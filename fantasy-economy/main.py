"""
Start the simulation
"""
import os

import duckdb
from flask import Flask, render_template

from kingdom import Kingdom
from simulation import simulate_day
from database import setup_database, save_daily_snapshot

app = Flask(__name__)

if not os.path.exists("fantasy-economy/data"):
    os.makedirs("fantasy-economy/data")
DB_PATH = "fantasy-economy/data/kingdom.duckdb"

# Make a database once
con = duckdb.connect(DB_PATH)
setup_database(con)

kingdom = Kingdom()
save_daily_snapshot(con, kingdom)

@app.route("/")
def kingdom_page():
    return render_template("kingdom.html", kingdom = kingdom, market_today=None)

@app.route("/market")
def market_page():
    return render_template(
        "market.html",
        kingdom=kingdom,
        market_today=None
    )

@app.route("/history")
def history_page():
    return render_template("history.html", kingdom=kingdom)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
