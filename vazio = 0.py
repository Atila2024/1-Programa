vazio = 0

tabuleiro = [[vazio for i in range(8)]for j in range(8)]

tabuleiro[0][0] = 1
tabuleiro[0][7] = 1
tabuleiro[7][0] = 1
tabuleiro[7][7] = 1
tabuleiro[3][4] = 1

for linha in tabuleiro:
    print(linha)
    
