def fibonacci(n):
    """
    Funkcja rekurencyjna obliczająca n-ty wyraz ciągu Fibonacciego.

    Parametry:
    - n (int): Numer wyrazu ciągu.

    Zwraca:
    - int: n-ty wyraz ciągu Fibonacciego.
    """
    if n <= 0:
        return "Podaj numer wyrazu większy od zera."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numer_wyrazu = 8

wyraz_fibonacci = fibonacci(numer_wyrazu)
print(f"{numer_wyrazu}-ty wyraz ciągu Fibonacciego: {wyraz_fibonacci}")
