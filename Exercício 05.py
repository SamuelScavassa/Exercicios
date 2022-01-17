

base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))


while True:
    if base <= 0 or altura <= 0:
        print('Dados inválidos')
        break
    area = base * altura / 2
    print(f'A área do triângulo é: {area}')
    break