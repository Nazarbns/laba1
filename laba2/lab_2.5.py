x = int(input("Podaj liczbę studentów: "))

suma_punktow = 0
licznik_studentow = 0

while licznik_studentow < x:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {licznik_studentow + 1}: "))
    suma_punktow += punkty
    licznik_studentow += 1

    srednia = suma_punktow / x
    print(f"Średnia liczba punktów w grupie wynosi: {srednia}")