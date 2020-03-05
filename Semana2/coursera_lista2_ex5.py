'''
Exercício 5 - Verificando ordenação

Receba 3 números inteiros na entrada e imprima
crescente
se eles forem dados em ordem crescente. Caso contrário, imprima 
não está em ordem crescente
'''

numb1 = int(input("Insira um número: "))
numb2 = int(input("Insira outro número: "))
numb3 = int(input("Insira o último número: "))

if (numb1 <= numb2) and (numb2 <= numb3):
    print("crescente")
else: 
    print("não está em ordem crescente")