# Recentemente Juquinha aprendeu a falar palavrões. Espantada com a descoberta do garoto, sua mãe o proibiu de falar qualquer palavrão, sobre o risco de o menino perder sua mesada.
# Como Juquinha odeia ficar sem mesada, ele te contratou para desenvolver um programa que informe para ele se uma palavra é um palavrão ou não. Palavrões são palavras que contém dez ou mais caracteres, todas as outras palavras são consideradas palavrinhas.

palavra = input('Digite a palavra: ')

if len(palavra) < 10:
  print('É uma palavrinha! :)')
else:
  print('É um palavrão! :o')
