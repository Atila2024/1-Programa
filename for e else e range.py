media = 0.0

for i in range(5):
    x = i + 1
    print("Prova",x,":",end=" ")
    nota=float(input(""))
    media += nota


print("\nMedia: ",round(media/5),"\n")
