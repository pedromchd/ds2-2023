# Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo.

def posNeg(n):
  if n < 0:
    print(f'{n} é negativo')
  else:
    print(f'{n} é positivo')

n = int(input('Insira número: '))
posNeg(n)
