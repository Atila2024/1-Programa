try:
    valor = int(input("Digite um numero:"))
    print("Resultado", 1/valor)
except ValueError:
    print("Tipo errado")
except ZeroDivisionError:
    print("Divisão por zero não permita")
except:
    printe("alguma outra exceção")
