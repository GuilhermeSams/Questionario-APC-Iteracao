'''Crie um programa que lê um número inteiro positivo n e realiza uma iteração que repete os seguintes passos:

Se n é zero, imprima "Ué? Já acabou?" e finalize a iteração.

Se n é par, imprima "Bom dia!".

Se n é impar, imprima "Boa noite!".

Ao fim de cada iteração, subtraia 1 de n.


A Entrada consiste de:
Um número inteiro positivo.

A Saída deve apresentar:
Uma série de mensagens, uma em cada linha, dependendo da entrada.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, foi digitado 1, retornando "Boa noite!" e "Ué? Já acabou?".
No segundo exemplo, foi digitado 2, retornando "Bom dia!", "Boa noite!" e "Ué? Já acabou?".
No terceiro exemplo, foi digitado 3, retornando "Boa noite!", "Bom dia!", "Boa noite!" e "Ué? Já acabou?".'''


n = int(input())
while True:
    if n == 0:
        n -= 1
        print("Ué? Já acabou?")
        break
    if n % 2 == 0:
        n -= 1
        print("Bom dia!")
    else:
        n -= 1
        print("Boa noite!")