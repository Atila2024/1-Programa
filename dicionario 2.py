dicionario = {"gato":"chat","cachorro":"chien","cavalo":"cheval"}
palavras = ["gato","leao","cavalo"]

for palavra in palavras:
    if palavras in dicionario:
        print(palavra,"-->",dicionario[palavra])
    else:
        print(palavra,"não esta no dicionario")
