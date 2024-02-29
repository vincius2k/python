x = 1    # int
y = 2.8  # float
z = 1j   # complex

#converter de int para float:
a = float(x)

#converter de float para int:
b = int(y)

#converter de int para complexo:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""Exemplo
Importe o módulo aleatório e exiba um número aleatório entre 1 e 9:"""
import random

print(random.randrange(1, 10))
