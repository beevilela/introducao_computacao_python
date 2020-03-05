'''
Exercício 1 - Distância entre dois pontos

Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto
'''

import math 

numbx1 = int(input("Insira um número: "))
numby1 = int(input("Insira mais um número: "))
numbx2 = int(input("Insira outro número: "))
numby2 = int(input("Insira o último número: "))

dist = math.sqrt((numbx1 - numbx2)**2 + (numby1 - numby2)**2)

if dist >= 10:
    print("longe")
else:
    print("perto")
