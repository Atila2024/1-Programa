turma = []
print(turma)


turma.append("Monica")
turma.append("Magali")
turma.append("Chico Bento")
print(turma)

for i in range(2):
    turma.append(input("Digite nome:"))
print(turma)


del turma[4]
del turma[3]
print(turma)


turma.insert(0, "Sansão")
print(turma)

print("Essa turma tem",len(turma),"menbros")
