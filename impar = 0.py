impar = 0
par = 0
num = int(input("Digite um numero ou 0 para sair:"))

while num != 0:
    if num % 2 == 1:
        impar += 1
    else:
        par += 1
    num = int(input("digite um numero ou 0 para sair"))

print("quantidade de numeros impares digitado:", impar)
print("Qunatidade de numeros pares digitados:", par)