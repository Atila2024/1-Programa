var = int(input("Digite um numero:"))
etapas = 0
if var == 0:
    print("Numero deve ser diferente de zero:")
else:
    while var != 1:
        if var % 2 == 0:
            var //= 2
        else:
            var = var*3+1
        print(var)
        etapas += 1
print("Etapas:", etapas)
