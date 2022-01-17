num = int(input('Digite um número: '))
numero = 1
if num > 0:
    for i in range(1, num + 1):
        for x in range(0, i):
            print(numero, end=' ')
            numero += 1
        print('\n')
