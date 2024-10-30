lista_1 = [1]
lista_2 = lista_1
lista_1[0] = 2
print(lista_2)

lista_1 = [1]
lista_2 = lista_1[:]
lista_1[0] = 2
print(lista_2)
