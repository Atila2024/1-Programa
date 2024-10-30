num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo:"))
num3 = int(input("Digite o terceiro:"))

maior_num = num1

if num2 > maior_num:
    maior_num = num2

if num3 > maior_num:
    maior_num = num3


print("O maior numero digitado foi", maior_num)
