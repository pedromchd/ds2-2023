'''
Escreva uma função que receba a longitude do ponto inicial e do ponto de destino de um navio pirata, juntamente com sua velocidade (em Km/h). 
A função deve calcular e exibir a posição do navio ao final de cada dia de viagem, considerando que a rota será ao longo da linha do Equador e que a variação de Km para cada grau de longitude é constante. 
Suponha que um grau de longitude corresponda a 111 Km.
Os valores usados para testar a função podem estar incluídos diretamente no código (não precisam ser solicitados ao usuário).
A saída deve ser exibida como nos exemplos de saída abaixo e a localização deve ser apresentada como um ponto flutuante com duas casas depois da virgula ( . no Python).
'''

def posicao(longitude_inicial, longitude_destino, velocidade, graus_longitude = 111):
  longitude_viagem = longitude_destino - longitude_inicial
  distancia_viagem = longitude_viagem * graus_longitude
  horas_viagem = distancia_viagem / velocidade
  dias_inteiros = horas_viagem // 24

  km_dia = velocidade * 24
  graus_dia = km_dia / graus_longitude

  dia = 1
  while dia <= dias_inteiros:
    posicao_dia = longitude_inicial + graus_dia * dia
    print(f'No final do dia {dia}, a posição do navio é {posicao_dia:.2f} graus de longitude.')
    dia += 1
  # endwhile #
  print(f'No final do dia {dia}, a posição do navio é {longitude_destino} graus de longitude.')

posicao(10, 210, 100)
print()
posicao(10, 360, 200)
