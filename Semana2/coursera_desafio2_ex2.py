'''
Exercício 2 - Desafio da videoaula

Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
O programa deve receber os parâmetros a, b e c da equação ax^2 + bx + c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:
esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima:
a raiz desta equação é X
onde X é o valor da raiz

Quando houver duas raízes reais imprima:
as raízes da equação são X e Y
onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente. Exemplos:
as raízes da equação são 1.0 e 2.0
as raízes da equação são -2.0 e 0.0
'''

import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta = (b**2) - (4 * a * c)

if delta > 0:
    raiz1 = (-b) + math.sqrt(delta)/ (2*a)
    raiz2 = (-b) - math.sqrt(delta)/ (2*a)
    if raiz1 >= raiz2 and raiz1 > 0:
        print("as raízes da equação são", raiz2, "e", raiz1)
    else:
        print("as raízes da equação são", raiz2, "e", raiz1)
else:
    if delta == 0:
        raiz = - (b) / (2*a)
        print("a raiz desta equação é", raiz)
    else:
        print("esta equação não possui raízes reais")
        