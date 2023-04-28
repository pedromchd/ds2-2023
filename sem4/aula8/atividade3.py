# Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def lim(n1, n2, li):
  if n1 + n2 > li:
    return True

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
li = int(input('Limite: '))

print(lim(n1, n2, li))
