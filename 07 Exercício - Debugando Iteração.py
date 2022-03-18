'''O seguinte programa Python deveria imprimir o valor final da soma. Depure o programa para que ele funcione
corretamente.

N = int(input())
i = 0
soma = "0"
while i < N:
    x = int(input())
    soma = soma + x
    i = 1
    print(soma)

Entrada

A entrada contém várias linhas: a primeira linha contém a quantidade de números inteiros a serem somados e as linhas
restantes os números inteiros, um por linha.

Saída

A soma dos números inteiros.

Observações

Os exemplos são autoexplicativos.'''


qntd_num = int(input())
soma = 0
cont = 0
while cont < qntd_num:
    n = int(input())
    cont += 1
    soma += n
print(soma)
