wiek =int(input("Podaj wiek: "))
print(wiek)

if wiek <0 :
    print("Wprowadziłeś/łaś niepoprawne dane")
elif wiek <= 4:
    print("Wejście za darmo")
elif wiek <= 18:
    print("Wejście za 10 złotych")
else:
    print("Wejście za 10 złotych")