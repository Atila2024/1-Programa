# indetificar o maior numero da lista

lista = [7, 3, 11, 5, 1, 9, 7, 15, 13]
maior = lista[0]

for i in lista:
    if i > maior:
        maior = i

print(maior)
