# Crie um programa que pede ao usuário para digitar o nome de um animal e verifica
# se ele é um gato, cachorro ou outro animal. Se for um gato, imprima na tela ”O
# animal é um gato”. Se for um cachorro, imprima na tela ”O animal é um cachorro”.
# Se for outro animal, imprima na tela ”O animal não é um gato nem um cachorro”.

animal = input('Diga o nome de um animal: ').lower()
match animal:
  case 'gato':
    print('O animal é um gato!')
  case 'cachorro':
    print('O animal é um cachorro!')
  case _:
    print('O animal não é um gato nem um cachorro...')
