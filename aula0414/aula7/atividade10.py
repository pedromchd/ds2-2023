# Dada uma string s, retorne uma string onde todas as ocorrências do primeiro caracter de s foram substituidas por ‘*’, exceto a primeira.
# Exemplo: ‘babble’ retorna ‘ba**le’
# Assuma que a string tem tamanho 1 ou maior. Dica: s.replace(stra, strb) retorna uma versão da string s onde todas as instancias de stra foram substituidas por strb.

s = input('Insira uma string qualquer: ')
sa = s[1:]
sb = s[0] + sa.replace(s[0], '*')

print(sb)
