def analizuj_string(tekst):
    """
    Funkcja analizująca string i zwracająca liczbę wielkich i małych liter oraz liczbę
    pozostałych znaków w postaci słownika.

    Parametry:
    - tekst (str): String do analizy.

    Zwraca:
    - dict: Słownik zawierający liczbę wielkich liter, małych liter i pozostałych znaków.
    """
    wyniki = {
        'wielkie_litery': 0,
        'male_litery': 0,
        'pozostale_znaki': 0
    }

    for znak in tekst:
        if znak.isupper():
            wyniki['wielkie_litery'] += 1
        elif znak.islower():
            wyniki['male_litery'] += 1
        else:
            wyniki['pozostale_znaki'] += 1

    return wyniki

przykladowy_tekst = "Hello World! 123"

wyniki_analizy = analizuj_string(przykladowy_tekst)
print(wyniki_analizy)
