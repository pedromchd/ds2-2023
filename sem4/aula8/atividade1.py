# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def min(n1, n2):
  if n1 < n2:
    print(n1)
  elif n2 < n1:
    print(n2)
  else:
    print('Os dois são iguais')

n1 = int(input('Insira número 1: '))
n2 = int(input('Insira número 2: '))

min(n1, n2)
