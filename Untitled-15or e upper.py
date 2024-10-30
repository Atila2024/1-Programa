palavra = input("Digite uma palavra:")
palavra = palavra.upper()
consoantes = ""

for letra in palavra:
    if letra == "A":
        continue
    if letra == "E":
        continue
    if letra == "I":
        continue
    if letra == "O":
        continue
    if letra == "U":
        continue
    consoantes += letra
    
print(consoantes)
 