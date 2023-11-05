distance = float(input("Droga pokonana: "))
fuel_consumption = float(input("Średnie spalanie (w litrach na 100 km): "))
expected_fuel_consumption = distance * fuel_consumption / 100
print(f"Eśli przejedziesz {distance} km, wtedy przewidywane zużycie paliwa będzie {expected_fuel_consumption} litrów.")
fuel_price = 6.5
trip_cost = fuel_price * expected_fuel_consumption
print(f"Koszt podróży {trip_cost} zl.")