Ano = int(input("Digite o Ano"))

if Ano < 1582:
    print("Fora do caledario gregoriano")
elif Ano % 4 != 0:
    print("Ano Comum")
elif Ano % 100 != 0:
    print("Ano bissexto")
elif Ano % 400 != 0:
    print("Ano Comum") 
else:
    print("Ano bissexto")   