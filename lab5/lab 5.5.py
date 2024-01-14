def oblicz_bmi(waga, wzrost):
    """
    Funkcja obliczająca wskaźnik BMI na podstawie wagi i wzrostu.

    Parametry:
    - waga (float): Waga w kilogramach.
    - wzrost (float): Wzrost w metrach.

    Zwraca:
    - float: Wskaźnik BMI.
    """
    bmi = waga / (wzrost ** 2)
    return bmi

def interpretuj_bmi(bmi):
    """
    Funkcja interpretująca wskaźnik BMI i informująca użytkownika o zakresie.

    Parametry:
    - bmi (float): Wskaźnik BMI.

    Wydruk:
    - None: Funkcja nie zwraca wartości, tylko wyświetla informację.
    """
    if bmi < 18.5:
        print(f"Twoje BMI wynosi {bmi:.2f} - Niedowaga.")
    elif 18.5 <= bmi < 24.9:
        print(f"Twoje BMI wynosi {bmi:.2f} - Waga prawidłowa.")
    elif 25 <= bmi < 29.9:
        print(f"Twoje BMI wynosi {bmi:.2f} - Nadwaga.")
    else:
        print(f"Twoje BMI wynosi {bmi:.2f} - Otyłość.")

# Przykładowe użycie funkcji
waga_uzytkownika = 70
wzrost_uzytkownika = 1.75

bmi_uzytkownika = oblicz_bmi(waga_uzytkownika, wzrost_uzytkownika)
interpretuj_bmi(bmi_uzytkownika)
