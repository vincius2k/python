idade=25
nome="Vinicius"
altura=1.87
pessoa=["Vinicius","30","1.87"]
ano_nascimento=1994
salario=10000
temperaturas=("15ºC","25ºC","45ºC")
aprovado = True
reprovado = False
horas_trabalhadas = 8
nota1 = 75

print(pessoa)


# Adicionando uma nova idade à lista pessoa
pessoa.append(30)

# Removendo o elemento que representa a altura da lista pessoa
pessoa.remove("1.87")

# Imprimindo os elementos da lista pessoa em ordem reversa
print(pessoa[::-1])