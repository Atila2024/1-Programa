def minha_funcao():
    global var
    var = 2
    print("Dentro da função:", var)


var = 123
minha_funcao()
print("Fora da função:", var)
