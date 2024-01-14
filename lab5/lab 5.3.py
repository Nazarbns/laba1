#a

def wypisz_imie_i_wiek(imie, wiek):
    """
    Funkcja wypisująca imię i wiek na ekranie.

    Parametry:
    - imie (str): Imię osoby.
    - wiek (int): Wiek osoby.
    """
    print(f"Imię: {imie}, Wiek: {wiek}")

# Przykładowe użycie funkcji
wypisz_imie_i_wiek("Anna", 25)

# Wyświetlenie opisu funkcji
print(wypisz_imie_i_wiek.__doc__)


#b

def wypisz_imie_i_wiek(imie, wiek=20):
    """
    Funkcja wypisująca imię i wiek na ekranie.

    Parametry:
    - imie (str): Imię osoby.
    - wiek (int): Wiek osoby, domyślnie ustawiony na 20.
    """
    print(f"Imię: {imie}, Wiek: {wiek}")

# Przykładowe użycie funkcji
wypisz_imie_i_wiek("Anna")

# Można także podać wiek jako argument
wypisz_imie_i_wiek("Marek", 30)
