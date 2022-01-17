"""
for i in range(10, -1, -1):
    print(i)
    if i == 0:
        print('FIM')

"""

contador = 10

while contador >= 0:
    if contador == 0:
        print(contador)
        print('FIM')
        break
    print(contador)
    contador -= 1


