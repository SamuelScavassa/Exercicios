
senha = list(input('Digite sua senha: '))
char = ['$', '#', '@']
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(senha) < 5:
  print('Senha inválida')

  
elif len(senha) > 15:
  print('Senha inválida')
  

for i in range(len(senha)):
  if senha[i] in a:
    continue
  elif senha[i] in b:
    continue
  elif senha[i] in num:
    continue
  elif senha[i] in char:
    continue
else:
  print('Senha inválida')
  