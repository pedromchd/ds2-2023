# Faça um programa que recebe um valor n, inteiro e positivo, calcule e mostre a
# seguinte soma:
# s = 1 + 1/2 + 1/3 + 1/4 + . . . + 1/n

n = int(input('Digite o número n de somas: '))
soma = 0
for num in range(1, n + 1):
  soma += 1 / num
print(soma)
