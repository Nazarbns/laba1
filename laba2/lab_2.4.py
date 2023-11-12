a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if a < b:
    mniejsza = a
    wieksza = b
else:
    mniejsza = b
    wieksza = a

print("Liczby parzyste: ")

for liczba in range(mniejsza, wieksza + 1):

    if liczba % 2 != 0:
        continue

    print(liczba)