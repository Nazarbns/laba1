def potega(a, n):
    """
    Funkcja rekurencyjna obliczająca n-ty stopień potęgi liczby a.

    Parametry:
    - a (float lub int): Podstawa potęgi.
    - n (int): Wykładnik potęgi.

    Zwraca:
    - float lub int: Wynik potęgowania.
    """
    if n == 0:
        return 1
    elif n > 0:
        return a * potega(a, n - 1)
    else:
        return 1 / (a * potega(a, -n - 1))

podstawa = 2
wykladnik = 3

wynik_potegi = potega(podstawa, wykladnik)
print(f"{podstawa}^{wykladnik} = {wynik_potegi}")
