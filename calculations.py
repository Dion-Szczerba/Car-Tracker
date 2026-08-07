from database import get_connection

connection = get_connection()
cursor = connection.cursor()

def calculate_mpg(fuel_ups):
    previous_row = None  # Initialize previous_row as None
    litres = 0 
    mpg_results = []  # List to store MPG results
    for row in fuel_ups:
        if previous_row is None:
            previous_row = row
            continue 
        elif row["is_full_tank"] == 0:
            litres += row["litres"]
            continue  # Skip this iteration if it's not a full tank
        else:
            distance = row["odometer"] - previous_row["odometer"]
            fuel_consumed = litres + row["litres"]  # Add the litres from the current full tank
            litres = 0  # Reset litres for the next calculation
            gallons_consumed = fuel_consumed / 4.54609  # Convert litres to gallons
            mpg = distance / gallons_consumed if gallons_consumed != 0 else 0
            mpg_results.append((distance, fuel_consumed, mpg))  # Store the result
            previous_row = row
    return mpg_results  # Return the list of MPG results

def get_fuel_ups(vehicle_id):
    cursor.execute("SELECT litres, odometer, is_full_tank FROM fuel_ups WHERE vehicle_id = ? ORDER BY odometer ASC", (vehicle_id,))
    return cursor.fetchall()



if __name__ == "__main__":
    fuel_ups = get_fuel_ups(1)  # Replace 1 with the actual vehicle_id you want to query
    results = calculate_mpg(fuel_ups)
    for distance, fuel_consumed, mpg in results:
        print(f"Distance: {distance} miles, Fuel Consumed: {fuel_consumed:.2f} litres, MPG: {mpg:.2f}")