'''
Exercício 1 - Par ou ímpar?

Receba um número inteiro na entrada e imprima

par 

quando o número for par ou

ímpar

quando o número for ímpar.
'''

numb = int(input("Insira um número: "))
if numb % 2 == 0:
    print("par")
else:
    print("ímpar")