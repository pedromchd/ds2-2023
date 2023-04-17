# Faça um programa para calcular n! (fatorial de n), sendo que o valor inteiro de n será fixado no programa
# Sabe-se que:
# n! = 1 ∗ 2 ∗ 3 ∗ · · · ∗ (n − 1) ∗ n
# 0! = 1, por definição

num = int(input('Calcular o fatorial do número: '))

fatorial = 1

for n in range(2, num + 1):
  fatorial *= n

print(fatorial)
