import duckdb

# Connect to a database file
con = duckdb.connect("groceries.duckdb")

# Create a table
# con.execute("""
#     CREATE TABLE IF NOT EXISTS groceries (
#         id INTEGER PRIMARY KEY,
#         item VARCHAR,
#         category VARCHAR,
#         quantity INTEGER,
#         price DECIMAL(10, 2)
#     )
# """)
# print("Database and table created!")

# con.execute("""
#     INSERT INTO groceries
#     VALUES
#         (1, 'Apples', 'Fruit', 6, 2.50),
#         (2, 'Bread', 'Bakery', 1, 1.80),
#         (3, 'Milk', 'Dairy', 2, 1.40),
#         (4, 'Carrots', 'Vegetables', 5, 1.20)
# """)

result = con.execute("""
    SELECT *
    FROM groceries
""").fetchall()
print(result)

new_item = "Bananas"
new_category = "Fruit"
new_quantity = 8
new_price = 1.75

con.execute("""
    INSERT INTO groceries
        (id, item, category, quantity, price)
    VALUES (?, ?, ?, ?, ?)
""", [
    5,
    new_item,
    new_category,
    new_quantity,
    new_price
])

result = con.execute("""
    SELECT *
    FROM groceries
""").fetchall()
print(result)


print("Database and table created!")

con.close()