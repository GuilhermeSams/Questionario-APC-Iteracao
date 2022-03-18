'''Faça um programa que leia uma string, que é o nome de uma marca de roupa. Se a string for "iken", imprima "apenas nao
 faca!", se a string for "sadida", imprima "tudo eh impossivel!". Caso a string não seja de nenhuma dessas duas marcas,
 apenas termine o programa.

Entrada

A entrada contém várias linhas, cada linha contém uma string com uma marca de roupa, menos a última. É garantido que
todas as strings da entrada são compostas por letras minúsculas.

Saída

Para cada marca de roupa, imprima a mensagem especificada.

Observações

No primeiro exemplo de teste, há apenas uma linha na saída pois a primeira linha é "sadida", mas a segunda não é
"sadida", nem "iken".'''


while True:
    marca = str(input())
    if marca == 'iken':
        print("apenas nao faca!")
    elif marca == 'sadida':
        print("tudo eh impossivel!")
    else:
        break
