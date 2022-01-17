numero = int(input('Digite um número inteiro: '))
contador = int(1) 
soma = int(0)
while True:
    if numero > contador:
        soma = soma + (numero * (numero -1))
        contador = contador + 1
        break
    print(f'O fatorial é {soma}')