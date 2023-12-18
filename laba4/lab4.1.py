#Zadanie 1
listaImion=("Asia","Bartek","Zosia","Waldek")
#a
print(type(listaImion))
posortowanaListaImion=sorted(listaImion, )
#b
posortowanaListaImion.append("Mati")
posortowanaListaImion.append("Dorota")
print(posortowanaListaImion.pop())
#c
posortowanaListaImion.insert(3,"Kasia")
#d
posortowanaListaImion.reverse()
print(posortowanaListaImion)
lista2x=posortowanaListaImion * 2
print(lista2x)
lista2x.sort()
print(lista2x)
