'''- Resolva os exercícios usando os conceitos de Programação Orientada a
     Objetos (POO) e a linguagem Python.

1. Crie uma classe com o método construtor e pelo menos três atributos.
   E use todos os atributos com valor default (padrão).

2. Crie os métodos gets e sets de todos os atributos.

3. Faça pelo menos uma crítica (validação) nos métodos sets.

4. Crie pelo menos três métodos funcional, ou seja, mais três métodos além dos métodos gets e sets.

5. Sobrescreva o método nativo do Python __str__ , ele deve retornar os atributos concatenados.

6. No método main, teste (use) a classe criada, crie pelo menos quatro objetos dessa classe,
   um objeto passando três argumentos, um objeto passando dois argumentos, um objeto passando
   um argumento e um objeto sem passar nenhum argumento.

7. No main, e teste (use) todos os métodos desenvolvidos na classe.
'''

import datetime

class Cadeiras:

    def __init__(self, unidades=0, tamanho=0, preco=0, ano_de_fabricacao=0):
        self.unidades = unidades
        self.tamanho = tamanho
        self.preco = preco
        self.ano_de_fabricacao = ano_de_fabricacao
#----------------------------------------------------------------------------------------
    def get_unidades(self):
        return self.unidades

    def set_unidades(self, nova_quantidade_unidades):
        if nova_quantidade_unidades > 0:
            self.unidades = nova_quantidade_unidades
        else:
            print('ERRO! Valor muito baixo!')

    def get_tamanho(self):
        return self.tamanho

    def set_tamanho(self, novo_tamanho):
        if novo_tamanho > 0:
            self.tamanho = novo_tamanho
        else:
            print('ERRO! Valor muito baixo!')

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
        else:
            print('ERRO! Valor muito baixo!')

    def get_ano_de_fabricacao(self):
        return self.ano_de_fabricacao

    def set_ano_de_fabricacao(self, novo_ano_de_fabricacao):
        if novo_ano_de_fabricacao > 0:
            self.ano_de_fabricacao = novo_ano_de_fabricacao
        else:
            print('ERRO! Valor muito baixo!')
#----------------------------------------------------------------------------------------
    def mostra_dados(self):
            print('A quantidade de cadeiras é: {}'.format(self.unidades))
            print('O tamanho das cadeiras é: {} cm'.format(self.tamanho))
            print('O preco das cadeiras é: R${}'.format(self.preco))
            print('O ano de fabricacao das cadeiras é: {}'.format(self.ano_de_fabricacao))

    def aumenta_valor(self, aumenta_valor):
        self.preco = self.preco + aumenta_valor

    def calcula_anos(self):
        hoje = datetime.date.today().year
        anos = hoje - self.ano_de_fabricacao
        return anos
#----------------------------------------------------------------------------------------
    def __str__(self):
        variavel = f'{self.unidades} unidades, {self.tamanho} cm, R${self.preco}, {self.ano_de_fabricacao}'
        return variavel
#----------------------------------------------------------------------------------------
    def input_novas_unidades(self):
        novas_unidades = int(input('Digite a nova quantidade de cadeiras: '))
        return novas_unidades
    def input_novo_tamanho(self):
        novo_tamanho = int(input('Digite o novo tamanho das cadeiras em cm: '))
        return novo_tamanho
    def input_novo_preco(self):
        novo_preco = float(input('Digite o novo preco das cadeiras: '))
        return novo_preco
    def input_novo_ano_de_fabricacao(self):
        novo_ano_de_fabricacao = int(input('Digite o novo ano de fabricacao: '))
        return novo_ano_de_fabricacao

if __name__ == '__main__':
    print('                  -> C A D E I R A S <-')
    print('-=-' * 20)
    cadeiras1 = Cadeiras(200, 120, 2000, 2018)
    cadeiras2 = Cadeiras(150, 110, 1650)
    cadeiras3 = Cadeiras(100, 125)
    cadeiras4 = Cadeiras(300)
    cadeiras5 = Cadeiras()
#----------------------------------------------------------------------------------------
    print('ESTOQUE 1')
    cadeiras1.mostra_dados()
    print('---' * 20)
    print('ESTOQUE 2')
    cadeiras2.mostra_dados()
    print('---' * 20)
    print('ESTOQUE 3')
    cadeiras3.mostra_dados()
    print('---' * 20)
    print('ESTOQUE 4')
    cadeiras4.mostra_dados()
    print('---' * 20)
    print('ESTOQUE 5')
    cadeiras5.mostra_dados()
    print('-=-' * 20)
#----------------------------------------------------------------------------------------
    aumenta_valores = float(input('Digite o preco que gostaria de aumentar nos produtos: '))
    print(' ALTERACAO - ESTOQUE 1')
    estoque1_1 = cadeiras1.input_novas_unidades()
    cadeiras1.set_unidades(estoque1_1)

    estoque1_2 = cadeiras1.input_novo_tamanho()
    cadeiras1.set_tamanho(estoque1_2)

    cadeiras1.aumenta_valor(aumenta_valores)

    estoque1_3 = cadeiras1.input_novo_ano_de_fabricacao()
    cadeiras1.set_ano_de_fabricacao(estoque1_3)

    print('---' * 20)
    print(' ALTERACAO - ESTOQUE 2')
    estoque2_1 = cadeiras2.input_novas_unidades()
    cadeiras2.set_unidades(estoque2_1)

    estoque2_2 = cadeiras2.input_novo_tamanho()
    cadeiras2.set_tamanho(estoque2_2)

    cadeiras2.aumenta_valor(aumenta_valores)

    estoque2_3 = cadeiras2.input_novo_ano_de_fabricacao()
    cadeiras2.set_ano_de_fabricacao(estoque2_3)

    print('---' * 20)
    print(' ALTERACAO - ESTOQUE 3')
    estoque3_1 = cadeiras3.input_novas_unidades()
    cadeiras3.set_unidades(estoque3_1)

    estoque3_2 = cadeiras3.input_novo_tamanho()
    cadeiras3.set_tamanho(estoque3_2)

    cadeiras3.aumenta_valor(aumenta_valores)

    estoque3_3 = cadeiras3.input_novo_ano_de_fabricacao()
    cadeiras3.set_ano_de_fabricacao(estoque3_3)

    print('---' * 20)
    print(' ALTERACAO - ESTOQUE 4')
    estoque4_1 = cadeiras4.input_novas_unidades()
    cadeiras4.set_unidades(estoque4_1)

    estoque4_2 = cadeiras4.input_novo_tamanho()
    cadeiras4.set_tamanho(estoque4_2)

    cadeiras4.aumenta_valor(aumenta_valores)

    estoque4_3 = cadeiras4.input_novo_ano_de_fabricacao()
    cadeiras4.set_ano_de_fabricacao(estoque4_3)

    print('---' * 20)
    print(' ALTERACAO - ESTOQUE 5')
    estoque5_1 = cadeiras5.input_novas_unidades()
    cadeiras5.set_unidades(estoque5_1)

    estoque5_2 = cadeiras5.input_novo_tamanho()
    cadeiras5.set_tamanho(estoque5_2)

    cadeiras5.aumenta_valor(aumenta_valores)

    estoque5_3 = cadeiras5.input_novo_ano_de_fabricacao()
    cadeiras5.set_ano_de_fabricacao(estoque5_3)
#----------------------------------------------------------------------------------------
    print('-=-' * 20)
    print('ESTOQUE 1 - ATUALIZADO')
    print(cadeiras1)
    print('As cadeiras tem exatos {} ano(s) de fabricacao!'.format(cadeiras1.calcula_anos()))

    print('---' * 20)
    print('ESTOQUE 2 - ATUALIZADO')
    print(cadeiras2)
    print('As cadeiras tem exatos {} ano(s) de fabricacao!'.format(cadeiras2.calcula_anos()))

    print('---' * 20)
    print('ESTOQUE 3 - ATUALIZADO')
    print(cadeiras3)
    print('As cadeiras tem exatos {} ano(s) de fabricacao!'.format(cadeiras3.calcula_anos()))

    print('---' * 20)
    print('ESTOQUE 4 - ATUALIZADO')
    print(cadeiras4)
    print('As cadeiras tem exatos {} ano(s) de fabricacao!'.format(cadeiras4.calcula_anos()))

    print('---' * 20)
    print('ESTOQUE 5 - ATUALIZADO')
    print(cadeiras5)
    print('As cadeiras tem exatos {} ano(s) de fabricacao!'.format(cadeiras5.calcula_anos()))

#----------------------------------------------------------------------------------------
# O.B.S. -> Caso eu fosse chamar os métodos gets para a cadeiras1, ficaria assim:

#     print(cadeiras1.get_unidades())
#     print(cadeiras1.get_tamanho())
#     print(cadeiras1.get_preco())
#     print(cadeiras1.get_ano_de_fabricacao())

# O.B.S. -> Eu só nao chamei todos os métodos gets, pois eu queria deixar o programa mais bonito visualmente.








