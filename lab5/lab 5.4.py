def sprawdz_czy_dodatnia(x):
    """
    Funkcja sprawdzająca, czy podana liczba jest dodatnia.

    Parametry:
    - x (float lub int): Sprawdzana liczba.
    """
    if x > 0:
        print(f"Liczba {x} jest dodatnia.")
    elif x == 0:
        print(f"Liczba {x} jest równa zeru.")
    else:
        print(f"Liczba {x} nie jest dodatnia.")

sprawdz_czy_dodatnia(5)
sprawdz_czy_dodatnia(0)
sprawdz_czy_dodatnia(-3)
