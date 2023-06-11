'''
- Resolva o exercício usando os conceitos de Programação
     Orientada a Objetos (POO) e a linguagem Python.

1. Crie uma classe com o método construtor e pelo menos dois atributos.

2. Crie os métodos gets e sets de todos os atributos.

3. No método main, teste (use) a classe criada, crie (instancie)
   pelo menos três objetos dessa classe e use (chame) todos os métodos
   desenvolvidos na classe.
'''

class Senadores:
    def __init__(self, nomeCompleto, idade, altura, partidoSigla):
        self.nome = nomeCompleto
        self.idade = idade
        self.altura = altura
        self.partido = partidoSigla

    def get_nome(self):
        return self.nome

    def set_nome(self, nome_novo):
        self.nome = nome_novo


    def get_idade(self):
        return self.idade

    def set_idade(self, idade_nova):
        self.idade = idade_nova


    def get_altura(self):
        return self.altura

    def set_altura(self, altura_nova):
        self.altura = altura_nova


    def get_partido(self):
        return self.partido

    def set_partido(self, partido_novo):
        self.partido = partido_novo

if __name__ == '__main__':
    senador1 = Senadores('José Mario da Costa', 65, 1.71, 'PSFG')
    senador2 = Senadores('Romário de Souza Faria', 57, 1.69, 'PL')
    senador3 = Senadores('Heitor Campos Melo', 54, 1.77, 'PTJ')
    senador4 = Senadores('Roberta da Silva Teixeira', 56, 1.80, 'PSG')

    print('---' * 20)
    print('              -== S E N A D O R E S ==-')
    print('---' * 20)
    print('Nome do Primeiro Senador: {}'.format(senador1.get_nome()))
    print('Idade do Primeiro Senador: {}'.format(senador1.get_idade()))
    print('Altura do Primeiro Senador: {}'.format(senador1.get_altura()))
    print('A Sigla do Partido do Primeiro Senador: {}'.format(senador1.get_partido()))
    print('---' * 20)
    print('Nome do Segundo Senador: {}'.format(senador2.get_nome()))
    print('Idade do Segundo Senador: {}'.format(senador2.get_idade()))
    print('Altura do Segundo Senador: {}'.format(senador2.get_altura()))
    print('A Sigla do Partido do Segundo Senador: {}'.format(senador2.get_partido()))
    print('---' * 20)
    print('Nome do Terceiro Senador: {}'.format(senador3.get_nome()))
    print('Idade do Terceiro Senador: {}'.format(senador3.get_idade()))
    print('Altura do Terceiro Senador: {}'.format(senador3.get_altura()))
    print('A Sigla do Partido do Terceiro Senador: {}'.format(senador3.get_partido()))
    print('---' * 20)
    print('Nome do Quarto Senador: {}'.format(senador4.get_nome()))
    print('Idade do Quarto Senador: {}'.format(senador4.get_idade()))
    print('Altura do Quarto Senador: {}'.format(senador4.get_altura()))
    print('A Sigla do Partido do Quarto Senador: {}'.format(senador4.get_partido()))
    print('---' * 20)
# ------------------------------------------------------------------------------------------
    troca_nome1 = input('Digite o nome do novo Senador 1: ')
    troca_idade1 = input('Digite a nova idade do novo Senador 1: ')
    troca_altura1 = input('Digite a nova altura do novo Senador 1: ')
    troca_sigla1 = input('Digite a nova sigla do partido do novo Senador 1: ')
    print('---' * 20)
    senador1.set_nome(troca_nome1)
    print('Nome do Primeiro Senador: {}'.format(senador1.get_nome()))
    senador1.set_idade(troca_idade1)
    print('Idade do Primeiro Senador: {}'.format(senador1.get_idade()))
    senador1.set_altura(troca_altura1)
    print('Altura do Primeiro Senador: {}'.format(senador1.get_altura()))
    senador1.set_partido(troca_sigla1)
    print('A Sigla do Partido do Primeiro Senador: {}'.format(senador1.get_partido()))
    print('---' * 20)
# ------------------------------------------------------------------------------------------
    troca_nome2 = input('Digite o nome do novo Senador 2: ')
    troca_idade2 = input('Digite a nova idade do novo Senador 2: ')
    troca_altura2 = input('Digite a nova altura do novo Senador 2: ')
    troca_sigla2 = input('Digite a nova sigla do partido do novo Senador 2: ')
    print('---' * 20)
    senador2.set_nome(troca_nome2)
    print('Nome do Segundo Senador: {}'.format(senador2.get_nome()))
    senador2.set_idade(troca_idade2)
    print('Idade do Segundo Senador: {}'.format(senador2.get_idade()))
    senador2.set_altura(troca_altura2)
    print('Altura do Segundo Senador: {}'.format(senador2.get_altura()))
    senador2.set_partido(troca_sigla2)
    print('A Sigla do Partido do Segundo Senador: {}'.format(senador2.get_partido()))
    print('---' * 20)
#------------------------------------------------------------------------------------------
    troca_nome3 = input('Digite o nome do novo Senador 3: ')
    troca_idade3 = input('Digite a nova idade do novo Senador 3: ')
    troca_altura3 = input('Digite a nova altura do novo Senador 3: ')
    troca_sigla3 = input('Digite a nova sigla do partido do novo Senador 3: ')
    print('---' * 20)
    senador3.set_nome(troca_nome3)
    print('Nome do Terceiro Senador: {}'.format(senador3.get_nome()))
    senador3.set_idade(troca_idade3)
    print('Idade do Terceiro Senador: {}'.format(senador3.get_idade()))
    senador3.set_altura(troca_altura3)
    print('Altura do Terceiro Senador: {}'.format(senador3.get_altura()))
    senador3.set_partido(troca_sigla3)
    print('A Sigla do Partido do Terceiro Senador: {}'.format(senador3.get_partido()))
    print('---' * 20)
#------------------------------------------------------------------------------------------
    troca_nome4 = input('Digite o nome do novo Senador 4: ')
    troca_idade4 = input('Digite a nova idade do novo Senador 4: ')
    troca_altura4 = input('Digite a nova altura do novo Senador 4: ')
    troca_sigla4 = input('Digite a nova sigla do partido do novo Senador 4: ')
    print('---' * 20)
    senador4.set_nome(troca_nome4)
    print('Nome do Quarto Senador: {}'.format(senador4.get_nome()))
    senador4.set_idade(troca_idade4)
    print('Idade do Quarto Senador: {}'.format(senador4.get_idade()))
    senador4.set_altura(troca_altura4)
    print('Altura do Quarto Senador: {}'.format(senador4.get_altura()))
    senador4.set_partido(troca_sigla4)
    print('A Sigla do Partido do Quarto Senador: {}'.format(senador4.get_partido()))
    print('---' * 20)
