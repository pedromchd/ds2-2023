# Faça um programa que verifique e mostre os números entre 1000 e 2000 (inclusive)
# que, quando divididos por 11, produzam resto 5

for num in range(1000, 2001):
  if num % 11 == 5:
    print(num)
