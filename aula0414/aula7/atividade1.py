# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
# Saída:
# NOTAS:                 | MOEDAS:
# x nota(s) de R$ 100.00 | x moeda(s) de R$ 1.00
# x nota(s) de R$ 50.00  | x moeda(s) de R$ 0.50
# x nota(s) de R$ 20.00  | x moeda(s) de R$ 0.25
# x nota(s) de R$ 10.00  | x moeda(s) de R$ 0.10
# x nota(s) de R$ 5.00   | x moeda(s) de R$ 0.05
# x nota(s) de R$ 2.00   | x moeda(s) de R$ 0.01

valor = float(input('Insira um valor monetário: R$'))
valor = int(valor * 100)

notas = {100.00: 0, 50.00: 0, 20.00: 0, 10.00: 0, 5.00: 0, 2.00: 0}
moedas = {1.00: 0, 0.50: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}

for key in notas.keys():
  notas[key] = valor // int(key * 100)
  valor %= int(key * 100)
  print(f'{notas[key]} nota(s) de R${key:.2f}')

for key in moedas.keys():
  moedas[key] = valor // int(key * 100)
  valor %= int(key * 100)
  print(f'{moedas[key]} moeda(s) de R${key:.2f}')
