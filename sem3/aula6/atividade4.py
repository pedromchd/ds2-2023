# Crie um programa que solicite ao usuário para digitar uma lista de números e
# calcule a média desses números. O programa deve continuar a pedir números até
# que o usuário digite -1”para encerrar a entrada de números.

lista = []
while True:
  numero = int(input('Digite um número: '))
  if numero == -1:
    break
  lista.append(numero)

media = 0
for n in lista:
  media += n

print(f'A média destes números é {media / len(lista)}')
