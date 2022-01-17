# Exercício 12: Crie um programa que calcule o valor a ser pago por um produto considerando o seu preço 
# normal e a condição de pagamento: 
# à vista no dinheiro ou cheque: 10% de desconto;
# à vista no cartão: 5% de desconto;
# em até 2x no cartão: preço normal;
# em 3x no cartão: 20% de juros.

valor_normal = float(input('Digite o valor normal do produto em R$: '))
forma_pagamento = int(input('| Digite 1 para à vista no dinheiro ou cheque: | Digite 2 para à vista no cartão: |\n | Digite 3 para em até 2x no cartão | |Digite 4 para 3x no cartão| :  '))

if forma_pagamento == 1:
    valor_pago = valor_normal - (valor_normal * 0.1)
elif forma_pagamento == 2:
    valor_pago = valor_normal - valor_normal * 0.05
elif forma_pagamento == 3:
    valor_pago = valor_normal
elif forma_pagamento == 4:
    valor_pago = valor_normal + (valor_normal * 0.2)
else:
    print ('fORMA INVALIDA')

print(f'O valor a ser pago é {valor_pago}') 