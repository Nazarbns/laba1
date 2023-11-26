a=int(input("Podaj wysokość choinki: "))

for i in range(a):
    print(' '*(a-i-1) + '*'*(2*i+1))