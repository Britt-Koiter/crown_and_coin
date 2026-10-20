"""
Start the simulation
"""
import os

import duckdb
from flask import Flask, render_template, redirect, url_for, request

from kingdom import Kingdom
from simulation import simulate_day, trade
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
    market = get_market_today(con, kingdom.day)
    return render_template("kingdom.html", kingdom = kingdom, market_today=market)

@app.route("/market")
def market_page():
    market = get_market_today(con, kingdom.day)
    return render_template(
        "market.html",
        kingdom=kingdom,
        market_today=market
    )

@app.route("/history")
def history_page():
    return render_template("history.html", kingdom=kingdom)


@app.route("/advance-day", methods=["POST"])
def advance_day():
    simulate_day(con, kingdom)
    save_daily_snapshot(con, kingdom)

    return redirect(url_for("kingdom_page"))


def get_market_today(con, day):
    result = con.execute("""
        SELECT day, market_type, grain_price, wood_price, iron_price
        FROM markets
        WHERE day = ?
    """, [day]).fetchone()

    if result is None:
        return None

    return {
        "day": result[0],
        "name": result[1],
        "prices": {
            "grain": result[2],
            "wood": result[3],
            "iron": result[4]
        }
    }


@app.route("/trade", methods=["POST"])
def trade_route():
    action = request.form.get("action")
    resource = request.form.get("resource")
    quantity = request.form.get("quantity", type=int)

    market = get_market_today(con, kingdom.day)

    if market is None:
        return redirect(url_for("market_page"))

    try:
        success = trade(
            con,kingdom, market,
            action=action, resource=resource, quantity=quantity,
        )
    except ValueError as error:
        print(error)
        success = False

    if success:
        print("Trade successful!")
    else:
        print("Trade failed!")

    return redirect(url_for("market_page"))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
