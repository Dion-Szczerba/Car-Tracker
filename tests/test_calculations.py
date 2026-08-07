import calculations
import pytest

def test_calculate_mpg():
    fake_fuel_ups = [
        {"odometer": 98000, "litres": 40, "is_full_tank": 1},
        {"odometer": 98150, "litres": 15, "is_full_tank": 0},
        {"odometer": 98300, "litres": 25, "is_full_tank": 1},
    ]
    results = calculations.calculate_mpg(fake_fuel_ups)
    # one gap closes (98000 -> 98300): 300 miles, 40 litres
    distance, fuel, mpg = results[0]
    assert distance == 300
    assert fuel == 40