# Registro de temperatura
# 1 registro por hora
# 31 dia no mes
# 24* 31 = 744 valores por mes
# coluna:horas ( 24 colunas)


temp = [[0.0 for i in range(24)] for j in range(31)]

for i in range(31):
    temp[i][12] = 33.3


for linha in temp:
    print(linha)
