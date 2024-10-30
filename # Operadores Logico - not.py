# Operadores Logico - not
# Teste com 0,1,34 e 5

a = int(input("Digite valor A:"))


if a:
    print("0 - False")
else:
    print("1 - True")

print(a > 0)
print(not (a > 0))
print(a != 0)
print(not (a == 0))
y = not a
print(y)
z = not not a
print(z)
