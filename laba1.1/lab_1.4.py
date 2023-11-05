distance = int(input("Droga pokonana: "))
fuel_consumption = int(input("Średnie spalanie (w litrach na 100 km): "))
expected_fuel_consumption = distance * fuel_consumption / 100
print("Przewidywane zużycie paliwa będzie (litrów): ", expected_fuel_consumption)
fuel_price = 6.5
trip_cost = fuel_price * expected_fuel_consumption
print("Koszt podróży (zl):", trip_cost)