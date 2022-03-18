'''Na matemática, a Sequência de Fibonacci, é uma sequência de números inteiros, começando por 0, na qual, cada termo
subsequente corresponde à soma dos dois anteriores. Os números de Fibonacci são, portanto, os números que compõem a
seguinte sequência:

0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,…

Curioso com a Sequência de Fibonacci, onde cada termo subsequente corresponde à soma dos dois anteriores, e os dois
primeiros valores da sequência são 0 e 1, dessa vez você resolveu imprimir todos os valores da sequência. Implemente
uma função chamanda fibonacci que tem como parâmetro n e imprime os primeiros n-termos da sequência de fibonacci.


A Entrada consiste de:
A função fibonacci recebe como parâmetro um único inteiro 1≤n≤30 que indica a quantidade de termos da sequência.

A Saída deve apresentar:
Uma linha com todos os n termos da Sequência de Fibonacci, separados por espaços, conforme os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
 irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, o argumento é 2. Então foi calculado o Fibonacci de 0 e de 1.
No segundo exemplo, o argumento é 1. Então foi calculado o Fibonacci de 0.
No terceiro exemplo, o argumento é 10. Então foi calculado o Fibonacci de 0 a 9.'''


def fibonacci(N):
    cont_a = 0
    cont_b = 1
    cont = 3
    if N == 1:
        print(cont_a)
    else:
        print(f'{cont_a} {cont_b}', end=" ")
        while cont <= N:
            cont_c = cont_a + cont_b
            print(f'{cont_c}', end=" ")
            cont_a = cont_b
            cont_b = cont_c
            cont += 1


fibonacci(10)
