# Dada uma string s, retorne uma string feita com os dois primeiros e os dois ultimos caracteres da string original.
# Exemplo: ‘spring’ retorna ‘spng’. Entretanto, se o tamanho da string for menor que 2, retorne uma string vazia.

s = input('Insira uma string qualquer: ')
res = []

if not len(s) < 2:
  res = s[:2] + s[-1:-3:-1][::-1]

print(res)
