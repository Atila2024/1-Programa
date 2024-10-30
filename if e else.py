var = int(input("Digite um numero:"))
if var >= 20:
    print("Seu numero é maior ou igual a 20")
    if var <= 100:
        print("E menor ou igual a 100")
    else:
        print("E maior que 100")
else:
    if var < 10:
        print("Seu numero é menor que 10")
    else:
        print("Seu numero é maior que 10 e menor que 20")
