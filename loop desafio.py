senha = 777
print("""
+----------------------+
|    Bem vindo !!!     |
|   Adivinhe a senha   |
+----------------------+ """)

num = int(input("Digite a senha correta:"))
while num != senha:
    print("Ha ha ha! Voce esta preso no loop!")
    num = int(input("Digite a senha correta:"))
    print("\nMuito Bem ! esta certa senha!\n")
