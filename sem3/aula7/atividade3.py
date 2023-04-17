# Escreva um programa que simule um financiamento. O sistema recebe o valor que a pessoa deseja financiar, além da renda e número de parcelas que ele deseja fazer o financiamento. Supondo que não há juros no financiamento, mostre na tela se o usuário terá seu financiamento aprovado ou não. Caso seja aprovado, mostre o valor da parcela que o usuário deverá pagar. O financiamento do usuário só será aprovado se o valor da parcela não ultrapassar 30% da sua renda, bem como o número de parcelas escolhidas for no máximo 180.

valor = float(input('Valor para financiamento: R$'))
renda = float(input('Renda: R$'))
parcelas = int(input('Número de parcelas: '))

valorParcelas = valor / parcelas

if valorParcelas > renda * 0.30 or parcelas < 1 or 180 < parcelas:
  print('Financiamento não aprovado.')
else:
  print(f'Financiamento aprovado. O parcelamento será de {parcelas} vezes de R${valorParcelas:.2f}')
