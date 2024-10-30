# exemplos lista + for

quadrados = [x**2 for x in range(10)]
print(quadrados)

potenciação = [2**i for i in range(8)]
print(potenciação)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impar = [x for x in lista if x % 2 != 0]
print(impar)
