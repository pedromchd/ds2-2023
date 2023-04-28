# Escreva uma função que recebe como entrada um número inteiro positivo n e retorne a soma de todos os inteiros positivos menores ou iguais a n.

def sum(num):
  sum = 0
  for n in range(0, num + 1):
    sum += n
  return sum

num = int(input('Número: '))
print(sum(num))
