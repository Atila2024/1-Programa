minha_lista = [8, 10, 6, 2, 4]
troca = True

while troca:
    troca = False
    for i in range(len(minha_lista)-1):
        if minha_lista[i] > minha_lista[i+1]:
            troca = True
            minha_lista[i], minha_lista[i+1] = minha_lista[i+1], minha_lista[i]
print(minha_lista)
