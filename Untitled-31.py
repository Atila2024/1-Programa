x = input("Digite "m" para sistema metrico (kg e Metros) ou "i" para sistema imperial em (libras e pés)")

if x == i:
    libras = print(input(float("Digite seu peso em Libras:")))
    pes = print(input(float("Digite sua altura em pés:")))
else:
    kilos = print(input(float("Digite seu peso em Kilos:")))
    metros = print(input(float("Digite sua altura em metros:")))


imc1 = kilos/metros
imc2 = libras/metros

print("Seu IMC é:", imc1, S)
