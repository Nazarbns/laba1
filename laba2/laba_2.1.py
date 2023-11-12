
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if a < b:
    mniejsza = a
    wieksza = b
else:
    mniejsza = b
    wieksza = a

for liczba in range(mniejsza, wieksza + 1):
    print(liczba)
