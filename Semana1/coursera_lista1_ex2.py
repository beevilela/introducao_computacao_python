'''
Exercício 2
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:
Exemplo:
Entrada de Dados:
Digite a primeira nota: 4
Digite a segunda nota: 5
Digite a terceira nota: 6
Digite a quarta nota: 7
Saída de Dados:
A média aritmética é 5.5
'''

nota_1 = input("Insira a primeira nota: ")
nota_2 = input("Insira a segunda nota: ")
nota_3 = input("Insira a terceira nota: ")
nota_4 = input("Insira a quarta nota: ")
media = (float(nota_1) + float(nota_2) + float(nota_3) + float(nota_4)) / 4
print("A média aritmética é", media)


