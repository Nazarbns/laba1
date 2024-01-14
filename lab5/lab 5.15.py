def wspolne_elementy(seq1, seq2):
    """
    Funkcja zwracająca listę wspólnych dla dwóch obiektów iterowalnych wartości.

    Parametry:
    - seq1 (iterable): Pierwszy obiekt iterowalny.
    - seq2 (iterable): Drugi obiekt iterowalny.

    Zwraca:
    - list: Lista zawierająca wspólne wartości obu sekwencji.
    """
    return list(set(seq1) & set(seq2))

sekwencja1 = [1, 2, 3, 4, 5]
sekwencja2 = [3, 4, 5, 6, 7]

wspolne_wartosci = wspolne_elementy(sekwencja1, sekwencja2)
print("Wspólne wartości:", wspolne_wartosci)
