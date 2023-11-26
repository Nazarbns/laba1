n=int(input("Ile wyrazów ciągu obliczyć: "))
a=int(input("Podaj pierwszy wyraz ciągu: "))
r=int(input("Podaj róznice ciągu arytnetycznego: "))

for i in range(n):
    x=a+i*r
    print(x)