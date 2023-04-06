Listatwo = [1,2, 3,4,5,6,7,8,9,10]
listaInvertida = []
for i in range(0,len(Listatwo)):
    listaInvertida.append(Listatwo[len(Listatwo)-1])
    Listatwo.pop()

print(listaInvertida)