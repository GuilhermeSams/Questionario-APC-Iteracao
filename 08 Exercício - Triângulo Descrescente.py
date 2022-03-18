'''Triângulo Descrescente
Utilizando laços aninhados, receber um inteiro n do usuário e imprimir a seguinte estrutura (sem o parêntesis):

Se n for par:
(n) (n−2) (n−4) … (0)
(n−2) (n−4) … (0)
(n−4) … (0)
…
(0)

Se n for ímpar:
(n) (n−2) (n−4) … (1)
(n−2) (n−4) … (1)
(n−4) … (1)
…
(1)


A Entrada consiste de:
Um número inteiro 0<n≤100

A Saída deve apresentar:
O padrão conforme o apresentado e os exemplos a seguir, onde os números em uma linha estão todos separados por um
espaço.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
Os exemplos são auto-explicativos.'''
cont_par = 0

n = int(input())
for c in range(n, -1, -2):
    print(c,end=" ")

