# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de
# vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha
# 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final
# do mês.
# O salário fixo e o total de vendas devem ser tratados como pronto flutuante.
# A saída deve ser: “A remuneração final de nome é de R$ valor a receber.”

nome = input('Nome do vendedor: ')
salarioFixo = float(input('Salário fixo: R$'))
totalVendas = float(input('Total de vendas efetuadas: R$'))
comissaoVendas = totalVendas * 0.15
remuneracao = salarioFixo + comissaoVendas
print(f'A remuneração final de {nome} é de R${remuneracao:.2f}')
