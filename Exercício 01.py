
numeros = range(0, 20)
multiplos = list()
contador = 0
for i in numeros:
    if numeros[i] != 0 and numeros[i] % 3 == 0:
        multiplos.append(numeros[i])
        contador += 1
    elif contador == 5:
        print(multiplos)
        break
