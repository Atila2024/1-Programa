while True:
    try:
        valor = int(input("Digite um numero:"))
        print("Resultado",1/valor)
        break
    except (ValueError, ZeroDivisionError):
        print("Tipo errado ou divisâo por zero")
    except:
        print("Alguma outra exceção")
