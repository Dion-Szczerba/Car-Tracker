from database import get_connection

connection = get_connection()
cursor = connection.cursor()

# Inserting the first vehicle

cursor.execute(
    """
    INSERT INTO vehicles (make, model, year, purchase_price) 
    VALUES (?, ?, ?, ?)
    """,
    ("Mitsubishi","GTO", 1991, 8000)
)

vehicle_id = cursor.lastrowid # Auto-generated ID of the inserted vehicle
print(f"Inserted vehicle with ID: {vehicle_id}")

cursor.execute(
    """
    INSERT INTO fuel_ups (vehicle_id, date, odometer, litres, price_per_litre, total_cost, is_full_tank)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (vehicle_id, "2026-07-07", 98400, 20, 1.81, 36.20, 1)
)



connection.commit()
connection.close()
print("Done")
