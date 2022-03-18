'''O seguinte programa Python deveria ler uma sequência de números inteiros maiores que zero e parar ao leu um número
menor ou igual a zero. Ao final ele deve imprimir a média aritmética dos números pares da sequência.

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

x = int(input())
acumulador = 0
achou_par = False
while x > 0:
    achou_par = par(x)
    if achou_par:
        cont += 1
        acumulador = acumulador + 1
    x = int(input())
cont += 1
media_par = acumulador/cont
print(media_par)
Entrada

A entrada contém várias linhas, sendo cada linha um número inteiro maior que zero. A sequência de números termina com
um número menor ou igual a zero, que não faz parte da sequência.



Saída

A média aritmética dos números pares.



Observações

Os exemplos são autoexplicativos.'''


cont = 0
soma = 0
while True:
    n = int(input())
    if n == 0 or n < 0:
        break
    while n != 0:
        if n % 2 == 0:
            cont += 1
            soma += n
        break
if soma != 0:
    print(f'{soma / cont}')
else:
    print(0.0)
