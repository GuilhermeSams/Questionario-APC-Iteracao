'''Codifique um programa que leia uma quantidade n≥1 de números e diga qual é o menor e qual é o maior valor.

Entrada
A primeira linha contém um inteiro n≥1. As próximas n linhas contém inteiros −104≤x≤104.

Saída
Imprima o menor e maior valores da sequência, como é mostrado nos exemplos.

'''


qtde_num = int(input())
cont = 0
lista = []
while cont < qtde_num:
    n = int(input())
    cont += 1
    lista += [n]
print(f'Menor: {min(lista)}')
print(f'Maior: {max(lista)}')
