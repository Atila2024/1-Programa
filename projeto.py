x = input("Digite'm' para sistema metrico (KG e metros) ou'i' \
          para sistema imperial ( libras e pés): ")


def libras_to_kilos(x):
    kilos = x*0.453592
    return kilos


def pes_to_metros(y):
    metros = y*0.3048
    return metros


def imc(peso, altura):
    imc = round(peso/altura**2, 2)
    if imc < 18.5:
        print("Seu IMC é", imc, "- Classificação: magreza")
    elif imc >= 18.5 and imc <= 24.9:
        print("Seu IMC é", imc, "- Classificação: normal")
    elif imc >= 25 and imc <= 29.9:
        print("Seu IMC é", imc, "- Classicação: sobrepeso")
    elif imc >= 30 and imc <= 39.9:
        print("SEu IMC é", imc, "- Classificação: obsesidade")
    else:
        print("Seu IMC é", imc, "- Classicação:obsidade grave")


if x == 'i':
    peso = libras_to_kilos(float(input("Digite seu peso em libras:")))
    altura = pes_to_metros(float(input("Digite sua altura em pés:")))
    imc(peso, altura)
else:
    peso = float(input("Digite seu peso em kilos:"))
    altura = float(input("Digite sua altura metros:"))
    imc(peso, altura)
