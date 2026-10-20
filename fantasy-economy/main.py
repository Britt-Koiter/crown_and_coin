"""
Start the simulation
"""
import os

import duckdb
from flask import Flask, render_template, redirect, url_for

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


@app.route("/advance-day", methods=["POST"])
def advance_day():
    simulate_day(con, kingdom)
    save_daily_snapshot(con, kingdom)

    return redirect(url_for("kingdom_page"))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
