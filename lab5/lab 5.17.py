def czy_palindrom(slowo):
    """
    Funkcja sprawdzająca, czy dane słowo jest palindromem.

    Parametry:
    - slowo (str): Słowo do sprawdzenia.

    Zwraca:
    - bool: True, jeśli słowo jest palindromem, False w przeciwnym przypadku.
    """
    slowo = slowo.lower()
    slowo = ''.join(c for c in slowo if c.isalnum())
    return slowo == slowo[::-1]

slowo1 = "kajak"
slowo2 = "python"

print(f"Czy '{slowo1}' to palindrom? {czy_palindrom(slowo1)}")
print(f"Czy '{slowo2}' to palindrom? {czy_palindrom(slowo2)}")
