# Crie um algoritmo de uma calculadora simples, ele deve receber dois valores inteiros
# e ao final deve mostrar na tela o resultado da operação
# Exemplo:
# valores de entrada:
# 3
# 5
# A resposta deve ser:
# O resultado de 3 + 5 = 8, de 3 - 5 = 2, de 3 * 5 = 15 e de 3 / 5 = 0.6
# Os números e resultados devem ser substituídos pelos informados/calculados.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
divs = num1 / num2
print(f'O resultado de {num1} + {num2} é {soma}, de {num1} - {num2} = {subt}, de {num1} * {num2} = {mult} e {num1} / {num2} = {divs}')
