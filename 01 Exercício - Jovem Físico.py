'''Ao entrar em Ciência da Computação, houve um erro na matrícula de Zikarias e ele acabou sendo registrado em um
currículo bem antigo que exigia a disciplina Física 1! Que azar. Ele estava completamente perdido no seu primeiro
dever de casa e chegou na aula sem entregar nada. Seu professor ficou muito nervoso e decidiu dar uma lição nele.
Ele deu uma tarefa que ninguém poderia resolver. Você consegue ajudá-lo?

Você receberá um corpo estacionário no espaço e as forças que o afetam. O corpo estacionário pode ser considerado um
ponto material com coordenadas (0, 0, 0). Zikarias só precisa responder se as forças que afetam o corpo estão em
equilíbrio. "Fácil", pensou Zikarias, "Só precisamos conferir se a soma de todos os vetores é igual a 0". Só que
quando Zikarias foi resolver o problema, ele ficou abarrotado com tantas forças e desistiu, e é aí que você entra.
Escreva um programa que determine se um corpo está estacionário ou movendo de acordo com os vetores de forças.

A Entrada consiste de:
A primeira linha contém um inteiro 1≤n≤100 representando o número de vetores.
Depois, há n linhas contendo 3 inteiros cada: as coordenadas xi, yi, e zi do vetor de forças i aplicado ao corpo.

A Saída deve apresentar:
Uma única linha contendo a palavra " YES" (sem aspas duplas) se o corpo está estacionário ou "NO" (sem aspas duplas)
caso contrário.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, são solicitados 3 vetores. A soma de todas as coordenadas é igual 6 e, portanto, a resposta é
 'NO'.
No segundo exemplo, são solicitados 3 vetores. A soma de todas as coordenadas é igual a 0 e, portanto, a resposta é
'YES'.'''

num_vetores = int(input())
cont = 0
soma = 0
while cont < num_vetores:
    vet1, vet2, vet3 = map(int, input().split(" "))
    cont += 1
    soma += vet1 + vet2 + vet3
if soma == 0:
    print("YES")
else:
    print("NO")
