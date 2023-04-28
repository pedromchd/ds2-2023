# Escreva uma função que recebe um número como parâmetro, a função imprime ”Fizz”se o número for múltiplo de três, imprime ”Buzz”se o número for múltiplo de cinco, e imprime ”FizzBuzz”se o número for múltiplo de três e cinco. Caso o número não seja múltiplo nem de três nem de cinco, ele deve ser impresso. Note que, ao contrário das funções anteriores, sua função não deve retornar nada. Ela precisa simplesmente imprimir o que foi pedido.

def fizzBuzz(n):
  if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
  elif n % 3 == 0:
    print('Fizz')
  elif n % 5 == 0:
    print('Buzz')
  else:
    print(n)

n = int(input('Número: '))

fizzBuzz(n)
