# Faça um programa que peça ao usuário para digitar a sua idade e verifique se ele é
# maior de idade ou não. Se for maior de idade, imprima na tela ”Você é maior de
# idade”, caso contrário, imprima ”Você é menor de idade”.

idade = int(input('Insira sua idade: '))
if idade >= 18:
  print('Vocé é maior de idade.')
else:
  print('Vocé é menor de idade.')
