def funcao_lista(n):
    lista = []
    for i in range(0, n):
        lista.insert(0, i)
    print("Print da função:", lista)
    return lista


x = funcao_lista(5)

print("Print do return:", x)
