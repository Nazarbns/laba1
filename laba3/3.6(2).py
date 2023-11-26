while True:
    a = int(input("Podaj liczbę: "))

    if a >= 0:
        print("To jest liczba")
    else:
        print(f"Pierwiastek kwadratowy z {a} = {abs(a)}")
        break

print("Dziękujemy za skorzystanie z naszej aplikacji")
