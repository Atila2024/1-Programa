var = int(input("Qual sua comida preferida?"))
if var <= 10:
    print("Seu numero é menor ou igual a 10")
elif var <= 20:
    print("Seu numero é maior que 10 e menor ou igual a 20")
elif var <= 40:
    print("Seu numero é maior que 20 e menor ou igual a 40")
elif var <= 60:
    print("Seu numero é maior que 40 e menor ou igual a 60")
elif var <= 80:
    print("Seu numero é maior que 60 e menor ou igual a 80")
else:
    print("seu numero é maior que 80")
