from database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT date, litres, total_cost FROM fuel_ups WHERE vehicle_id = ? AND total_cost > ?", (1, 10))  # Replace 1 with the actual vehicle_id you want to query
rows = cursor.fetchall()

for row in rows:
    print(row["date"], "|", row["litres"], "litres |", "£", row["total_cost"])

connection.close()