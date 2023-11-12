x = int(input("Podaj liczbę studentów: "))

suma_punktow = 0
licznik_studentow = 0


while True:

    punkty = float(input(f"Podaj liczbę punktów dla studenta {licznik_studentow + 1}: "))


    if 0 <= punkty <= 100:
        suma_punktow += punkty
        licznik_studentow += 1
    else:
        print("Błędna wartość punktów. Podaj liczbę punktów w przedziale 0-100.")
        continue

    if licznik_studentow == x:
        break

srednia = suma_punktow / x

print(f"Średnia liczba punktów w grupie wynosi: {srednia}")
