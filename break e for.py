print("\nInstrução break")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro do loop:",i)
print("Fora do loop")

print("\nInstrução continue")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro do loop:",i)
    print("Fora do loop\n")
