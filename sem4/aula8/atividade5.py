# Escreva uma função que recebe como entrada uma lista de números e retorna True se um número passado como parâmetro está presente na lista.

def search(list, num):
  return num in list

list = []
while True:
  try:
    n = int(input('Número para lista (Ctrl+C para fechar): '))
    list.append(n)
  except KeyboardInterrupt:
    num = int(input('-\nNúmero para pesquisar: '))
    break

print(search(list, num))
