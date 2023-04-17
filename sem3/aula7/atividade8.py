# Dado um contador inteiro do numero de donuts, retorne uma string com o formato ‘Number of donuts: <count>’ onde <count> é o numero recebido. Entretanto, se o contador for 10 ou mais, use a palavra ‘many’ ao invés do contador.
# Exemplo: donuts(5) retorna ’Number of donuts: 5’ e donuts(23) retorna ’Number of donuts: many’

donuts = int(input('Type the number of donuts: '))

if donuts < 10:
  print(f'Number of donuts: {donuts}')
else:
  print('Number of donuts: many')
