import random
jogada_pc = random.randint(1, 3)

if jogada_pc == 1:
  jogadapc = 'pedra'
elif jogada_pc == 2:
  jogada_pc = 'papel'
else:
  jogada_pc = 'tesoura'


jogada_player = input('Digite pedra, papel ou tesoura: ')
print(f'O computador escolheu {jogadapc}')



if jogada_pc == 1 and jogada_player == 'tesoura':
  print('O computador ganhou')
elif jogada_pc == 1 and jogada_player == 'papel':
  print('O player ganhou')
elif jogada_pc == 1 and jogada_player == 'pedra':
  print('Empate')
elif jogada_pc == 3 and jogada_player == 'tesoura':
  print('Empate')
elif jogada_pc == 3 and jogada_player == 'papel':
  print('O computador ganhou')
elif jogada_pc == 3 and jogada_player == 'pedra':
  print('O player ganhou')
elif jogada_pc == 2 and jogada_player == 'papel':
  print('Empate')
elif jogada_pc == 2 and jogada_player == 'tesoura':
  print('O player ganhou')
elif jogada_pc == 2 and jogada_player == 'pedra':
  print('O computador ganhou')




