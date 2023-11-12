x = int(input("Podaj wartość x: "))
y = int(input("Podaj wartość y: "))
z = int(input("Podaj wartość z: "))
if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x
    print("Posortowane liczby od najmniejszej do największej:")
    print(x, y, z)