import time
t = int(input("Podaj sekundy: "))
while t > 0:
 print("Pozostało sekund:", t)
 time.sleep(1)
 t -= 1
print("Koniec!")