# Joãozinho quer calcular e mostrar a quantidade de litros de combustível gastos em
# uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria
# que você o auxiliasse através de um simples programa. Para efetuar o cálculo,
# deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante
# a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida,
# calcular quantos litros seriam necessários.
# Ao final mostre a seguinte mensagem: “A quantidade de gasolina é de consumo.”

tempoViagem = float(input('Tempo gasto na viagem (em horas): '))
velocidadeViagem = int(input('Velocidade média da viagem (em km/h): '))
distanciaViagem = velocidadeViagem * tempoViagem
gastoLitros = distanciaViagem / 12
print(f'A quantidade de gasolina é de {gastoLitros:.1f} litros')
