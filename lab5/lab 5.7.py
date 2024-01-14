def odwroc_string(tekst):
    """
    Funkcja odwracająca string.

    Parametry:
    - tekst (str): String do odwrócenia.

    Zwraca:
    - str: Odwrócony string.
    """
    return tekst[::-1]

tekst_do_odwrocenia = "Hello, World!"
odwrocony_tekst = odwroc_string(tekst_do_odwrocenia)

print(f"Oryginalny tekst: {tekst_do_odwrocenia}")
print(f"Odwrócony tekst: {odwrocony_tekst}")