''' 1 -Desenvolva o programa que faça a leitura de vários números digitados pelo
usuário e use o valor -1 como condição (flag) de saída da estrutura de repetição.
Na tela de saída, mostre a quantidade de números digitados e a soma dos valores digitados.
Obs.: resolva sem usar lista.'''

# soma_dos_numeros = 0
# quantidade_de_numeros = 0
#
# print('Digite [-1] como condição de saída.')
#
# while True:
#     valor = float(input('Digite um número: '))
#
#     if valor == -1:
#         print('-=-=-' * 10)
#         print('A quantidade de números é: {}'.format(quantidade_de_numeros))
#         print('A soma dos números é: {}'.format(soma_dos_numeros))
#         break
#     quantidade_de_numeros += 1
#     soma_dos_numeros += valor


''' 2 -Desenvolva o programa que faça a leitura de vários números digitados pelo
usuário e use o valor -1 como condição (flag) de saída da estrutura de repetição.
Na tela de saída, mostre a quantidade de números digitados e a soma dos valores digitados.
Obs.: resolva usando lista. '''

# print('Digite [-1] como condição de saída.')
#
# numeros = list()
#
# while True:
#     valor = float(input('Digite um número: '))
#     if valor == -1:
#         print('-=-=-' * 10)
#         print('A soma dos números é: {}'.format(soma))
#         print('A quantidade de números é: {}'.format(quantidade))
#         break
#
#     numeros.append(valor)
#     soma = sum(numeros)
#     quantidade = len(numeros)


''' 3 -Desenvolva o programa que leia vários números, armazene-os numa lista e mostre
estas informações:

a- Quantidade de elementos armazenados na lista;
b- Soma dos valores da lista; 
c- Maior valor da lista;
d- Menor valor da lista;
e- Produto dos números;
f- Crie o enunciado e a resposta de mais um item de exercício;
g- Crie o enunciado e a resposta de mais um item de exercício; '''

from math import prod

l_numeros = list()

print('Digite [0] como como condição de saída.')

while True:
    valor = float(input('Digite um número: '))
    if valor == 0:
        print('-=-=-' * 10)
        print('A quantidade de elementos armazenados na lista é: {}'.format(quantidade))
        print('A soma dos valores da lista é: {}'.format(soma))
        print('O MAIOR valor da lista é: {}'.format(maior))
        print('O MENOR valor da lista é: {}'.format(menor))
        print('O produto dos números da lista  é: {}'.format(produto))
        print('-=-=-' * 10)
        print('Os números da lista são: {}'.format(l_numeros))
        print('-=-=-' * 10)
        print('A soma do primeiro número da lista com o último é: {}'.format(soma_das_bordas))
        break

    l_numeros.append(valor)
    quantidade = len(l_numeros)
    soma = sum(l_numeros)
    maior = max(l_numeros)
    menor = min(l_numeros)
    produto = prod(l_numeros)

# f- Crie o enunciado e a resposta de mais um item de exercício;
# -> Print todos os números da lista

    imprimir = l_numeros

# g- Crie o enunciado e a resposta de mais um item de exercício;
# -> Some o primeiro item da lista com o último

    soma_das_bordas = l_numeros[0] + l_numeros[-1]