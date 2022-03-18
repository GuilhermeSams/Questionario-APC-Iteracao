'''Jordan quer resolver um problema muito interessante. Dadas as informações sobre o tamanho da população e a taxa de
crescimento anual de duas cidades quaisquer (A e B), ele gostaria de saber quando a cidade menor (sempre é a cidade A)
irá alcançar a cidade B em população (se é que vai alcançar). Sua tarefa é construir um programa que faça esses cálculos
, porém, em alguns casos o tempo pode ser muito grande, e Jordan não se interessa em saber exatamente o tempo para estes
 casos.


A Entrada consiste de:
A entrada contém 4 valores: dois inteiros (100≤PA,PB≤1000000) indicando respectivamente a população de A e B, e dois
valores (0.0≤T1,T2≤100.0), indicando respectivamente, em percentual, o crescimento populacional de A e B.

A Saída deve apresentar:
"Mais de um milenio." se a quantidade de anos for superior a 1000, "Vai alcancar em X ano(s).", onde X representa a
quantidade de anos para a população de A alcançar o tamanho da população de B, ou "A nunca alcancara B.", se a
população nunca for alcançar a população de B.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
A população é sempre um valor inteiro, portanto, um crescimento de 2.5% anual sobre uma população de 100 pessoas
resultará em 102 pessoas, e não 102.5 pessoas, enquanto um crescimento de 2.5% anual sobre uma população de 1000
pessoas resultará em 1025. Para coletar a parte inteira de um número em ponto flutuante, considere a utilização da
função int.

Descrição dos Exemplos:
No primeiro exemplo, a população da cidade A é de 100 pessoas e a da cidade B é de 150 pessoas. A taxa de crescimento
populacional da cidade 1 é de 1.0% ao ano e a população da cidade B não está crescendo. Então, em 50 anos o número da
população da cidade A irá ultrapassar o da população da cidade B.
No segundo exemplo, a população da cidade A é de 90000 pessoas e a da cidade B é de 120000 pessoas. A taxa de
crescimento populacional da cidade 1 é de 5.5% ao ano e a da população é de 3.5%. Então, em 16 anos o número da
população da cidade A irá ultrapassar o da população da cidade B.'''


pA, pB, percA, percB = input().split()
pA = int(pA)
pB = int(pB)
percA = float(percA)
percB = float(percB)

