while True:
    opcao = int(input('Digite a operação: \nAdição(1) \nSubtração(2) \nMultiplicação(3) \nDivisão(4) \nSaída(5) \n: '))
    if opcao == 5:
        print('Saindo')
        break

    num1 = int(input('Digite o número 1: '))
    num2 = int(input('Digite o número 2: '))

    if opcao == 1:
        print(f'A soma é :{num1 + num2}\n')
    elif opcao == 2:
        print(f'A subtração é: {num1 - num2}\n')
    elif opcao == 3:
        print(f'A multiplicação é:{num1 * num2}\n')
    elif opcao == 4:
        print(f'A divisão é : {num1 / num2}\n')
