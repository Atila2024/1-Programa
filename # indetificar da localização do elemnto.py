# indetificar da localização do elemnto

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
encontrar = 5
finalizado = False

for i in lista:
    finalizado = lista[i] == encontrar
    if finalizado:
        break

if finalizado:
    print("Elemento encontrado no indice:",i)
else:
    print("Elemento não encontrado")
