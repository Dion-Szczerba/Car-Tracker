from database import get_connection

connection = get_connection()
cursor = connection.cursor()

# Inserting the first vehicle



vehicle_id = cursor.lastrowid # Auto-generated ID of the inserted vehicle
print(f"Inserted vehicle with ID: {vehicle_id}")

cursor.execute(
    """
    INSERT INTO fuel_ups (vehicle_id, date, odometer, litres, price_per_litre, total_cost, is_full_tank)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (1, "2026-07-05", 98200, 20, 1.81, 36.20, 1)
)



connection.commit()
connection.close()
print("Done")
