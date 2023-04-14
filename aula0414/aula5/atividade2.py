# Você foi contratado por uma empresa de vendas para criar um programa que
# gerencie suas vendas. A empresa vende três tipos de produtos: camisetas, calças e
# sapatos.
# E que o valor de cada camiseta é R$20,00, cada calça custa R$50,00 e cada sapato
# custa R$100,00.
# O programa deve permitir que o usuário insira o número de cada produto vendido
# e, em seguida, calcular e exibir o total de vendas para cada produto e o total geral
# de vendas.

precos = {'camisetas': 20.00, 'calças': 50.00, 'sapatos': 100.00}
numVendasCamisetas = int(input('Número de camisetas vendidas: '))
numVendasCalcas = int(input('Número de calças vendidas: '))
numVendasSapatos = int(input('Número de sapatos vendidos: '))
totalCamisetas = precos['camisetas'] * numVendasCamisetas
totalCalcas = precos['calças'] * numVendasCalcas
totalSapatos = precos['sapatos'] * numVendasSapatos
totalVendas = totalCamisetas + totalCalcas + totalSapatos
print(f'Total de vendas de camisetas: R${totalCamisetas:.2f}')
print(f'Total de vendas de calças: R${totalCalcas:.2f}')
print(f'Total de vendas de sapatos: R${totalSapatos:.2f}')
print(f'Total geral de vendas: R${totalVendas:.2f}')
