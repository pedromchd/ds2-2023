# Verifique se os seguintes valores são truthy ou Falsy (deve ser mostrado o
# resultado):
# a ”abc”
# b range(0)
# c 123456.789
# d -5
# e None
# f not(False)
# g False
# h print()

print('a', bool('abc'))
print('b', bool(range(0)))
print('c', bool(123456.789))
print('d', bool(-5))
print('e', bool(None))
print('f', bool(not(False)))
print('g', bool(False))
print('h', bool(print()))
