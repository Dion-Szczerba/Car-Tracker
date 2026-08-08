from fastapi import FastAPI
import calculations

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car Tracker API!"}

@app.get("/vehicles/{vehicle_id}/mpg")
def read_mpg(vehicle_id: int):
    try:
        fuel_ups = calculations.get_fuel_ups(vehicle_id)
        results = calculations.calculate_mpg(fuel_ups)
        return {"vehicle_id": vehicle_id, "mpg_results": results}
    except Exception as e:
        return {"error": str(e), "type": type(e).__name__}