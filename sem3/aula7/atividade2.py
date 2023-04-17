# Crie um programa que recebe um número entre 1 e 12 e com o comando match case mostre na tela o mês por extenso.
# Exemplo: Se receber 1 deverá mostrar Janeiro.

mes = 0
while mes < 1 or 12 < mes:
  mes = int(input('Insira um número entre 1 e 12: '))

match mes:
  case 1:
    print('Janeiro')
  case 2:
    print('Fevereiro')
  case 3:
    print('Março')
  case 4:
    print('Abril')
  case 5:
    print('Maio')
  case 6:
    print('Junho')
  case 7:
    print('Julho')
  case 8:
    print('Agosto')
  case 9:
    print('Setembro')
  case 10:
    print('Outubro')
  case 11:
    print('Novembro')
  case 12:
    print('Dezembro')
  case _:
    print('Não é um mês')
