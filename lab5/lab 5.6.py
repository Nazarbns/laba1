def oblicz_pole_trojkata(a, b, c):
    """
    Funkcja obliczająca pole trójkąta na podstawie długości boków a, b i c.

    Parametry:
    - a (float): Długość boku a.
    - b (float): Długość boku b.
    - c (float): Długość boku c.

    Zwraca:
    - float: Pole trójkąta.
    """
    try:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Długości boków muszą być dodatnie.")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Podane długości boków nie spełniają warunku istnienia trójkąta.")

        s = (a + b + c) / 2
        pole = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        return pole

    except ValueError as e:
        print(f"Błąd: {e}")
        return None

bok_a = 3
bok_b = 4
bok_c = 5

pole = oblicz_pole_trojkata(bok_a, bok_b, bok_c)

if pole is not None:
    print(f"Pole trójkąta o bokach {bok_a}, {bok_b}, {bok_c} wynosi: {pole:.2f}")
