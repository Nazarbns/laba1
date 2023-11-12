num1 = float(input("Podaj argument 1: "))
num2 = float(input("Podaj argument 2: "))
operation = input("Jaką operację chcesz wykonać (dodawanie(1), odejmowanie(2), mnożenie(3), dzielenie(4), potęgowanie(5)): ")



if operation == "1":
    result = num1 + num2
elif operation == "2":
    result = num1 * num2
elif operation == "3":
    result = num1 * num2
elif operation == "4":
    result = num1 / num2
elif operation == "5":
    result = num1 ** num2

print("Wynik:", result)