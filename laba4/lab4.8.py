zdanie = input("Podaj zdanie: ")
wyrazy = zdanie.split()
zdanie_sformatowane = ' '.join(word.capitalize() for word in wyrazy)
print("Zdanie z każdym wyrazem zaczynającym się i kończącym wielką literą:")
print(zdanie_sformatowane)
ciag_znakow = input("Podaj ciąg znaków: ")
licznik_znakow = {}
ciag_zmieniony = ''
for znak in ciag_znakow:
    if znak in licznik_znakow:
        ciag_zmieniony += '@'
    else:
        licznik_znakow[znak] = 1
        ciag_zmieniony += znak
print("Zmieniony ciąg znaków:", ciag_zmieniony)