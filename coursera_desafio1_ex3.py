'''
Exercício 3

Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:
Exemplo 1:

Entrada de Dados:
Digite um número inteiro: 78615

Saída de Dados:
O dígito das dezenas é 1

Exemplo 2:

Entrada de Dados:
Digite um número inteiro: 2

Saída de Dados:
O dígito das dezenas é 0
'''

a = input("Digite um número inteiro:")
dig = int(a) // 10
a = str(dig)
print("O dígito das dezenas é", a[-1])