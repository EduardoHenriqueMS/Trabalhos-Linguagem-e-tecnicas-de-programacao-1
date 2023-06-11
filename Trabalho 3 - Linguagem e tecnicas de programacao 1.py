'''- Resolva os exercícios usando os conceitos de Programação Orientada
     a Objetos (POO) e a linguagem Python.

1. Crie uma classe com o método construtor e pelo menos três atributos.
   E use pelo menos dois atributos com valor default (padrão).

2. Crie os métodos gets e sets de todos os atributos.

3. Faça pelo menos uma crítica (validação) nos métodos sets.

4. Crie pelo menos dois métodos funcional, ou seja, mais dois
   métodos além dos métodos gets e sets.

5. No método main, teste (use) a classe criada, crie pelo menos três
   objetos dessa classe, um objeto passando três argumentos, um objeto
   passando dois argumentos e um objeto passando um argumento.

6. E teste (use) todos os métodos desenvolvidos na classe.
'''

class Cordas:
    def __init__(self, marca, espessura=0.00, comprimento=0.00, preco=0.00):
        self.marca = marca
        self.espessura = espessura
        self.comprimento = comprimento
        self.preco = preco

    # ========================================================================
    def get_marca(self):
        return self.marca

    def set_marca(self, nova_marca):
        if nova_marca == '':
            print('ERRO! Tente novamente!')
        else:
            self.marca = nova_marca

    def get_espessura(self):
        return self.espessura

    def set_espessura(self, nova_espessura):
        if nova_espessura <= 0:
            print('ERRO! Tente novamente!')
        else:
            self.espessura = nova_espessura

    def get_comprimento(self):
        return self.comprimento

    def set_comprimento(self, novo_comprimento):
        if novo_comprimento == '':
            print('ERRO! Tente novamente!')
        else:
            self.comprimento = novo_comprimento

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        if novo_preco <= 0:
            print('ERRO! Tente novamente!')
        else:
            self.preco = novo_preco

    #========================================================================
    def altera_marca(self):
        marca = str(input('Digite a nova marca: '))
        return marca

    def altera_espessura(self):
        espessura = int(input('Digite a nova espessura: '))
        return espessura

    def altera_comprimento(self):
        comprimento = int(input('Digite o novo comprimento: '))
        return comprimento
    # ========================================================================
    def mostra_dados(self):
        print('A nova Marca é: {}'.format(self.marca))
        print('A nova Espessura é: {} cm'.format(self.espessura))
        print('O novo Comprimento é: {} cm'.format(self.comprimento))
        print('O novo Preco é: R${}'.format(self.preco))

    def aumenta_valor(self, valor_aumentado):
        self.preco = self.preco + valor_aumentado
    # ========================================================================
if __name__ == '__main__':
    corda1 = Cordas('Everlaste', 1, 50, 10)
    corda2 = Cordas('Adidas', 3, 100)
    corda3 = Cordas('Nike', 5)
    corda4 = Cordas('Puma')

    print('-=-' * 30)
    print('                                     C O R D A S')
    print('-=-' * 30)

    print('OBS.: A [espessura] e o [comprimento] da corda estão em centímetros(cm)')

    print('-=-' * 30)
    print('A marca da primeira corda é: {}'.format(corda1.get_marca()))
    print('A espessura da primeira corda é: {}'.format(corda1.get_espessura()))
    print('O comprimento da primeira corda é: {}'.format(corda1.get_comprimento()))
    print('O preco da primeira corda é: {}'.format(corda1.get_preco()))

    print('-=-' * 30)
    print('A marca da segunda corda é: {}'.format(corda2.get_marca()))
    print('A espessura da segunda corda é: {}'.format(corda2.get_espessura()))
    print('O comprimento da segunda corda é: {}'.format(corda2.get_comprimento()))
    print('O preco da segunda corda é: {}'.format(corda2.get_preco()))

    print('-=-' * 30)
    print('A marca da terceira corda é: {}'.format(corda3.get_marca()))
    print('A espessura da terceira corda é: {}'.format(corda3.get_espessura()))
    print('O comprimento da terceira corda é: {}'.format(corda3.get_comprimento()))
    print('O preco da terceira corda é: {}'.format(corda3.get_preco()))

    print('-=-' * 30)
    print('A marca da quarta corda é: {}'.format(corda4.get_marca()))
    print('A espessura da quarta corda é: {}'.format(corda4.get_espessura()))
    print('O comprimento da quarta corda é: {}'.format(corda4.get_comprimento()))
    print('O preco da quarta corda é: {}'.format(corda4.get_preco()))

# -----------------------------------------------------------------------------------------
    print('-=-' * 30)
    aumenta_valores = float(input('Digite o preco que gostaria de aumentar nos produtos: R$'))
    print('-=-' * 30)
    print('-> CORDA 1 <-')
    print('Digite as novas medidas para a corda 1: ')
#-----------------------------------------------------------------------------------------
    marca1 = corda1.altera_marca()
    corda1.set_marca(marca1)
    # ===========================================
    espessura1 = corda1.altera_espessura()
    corda1.set_espessura(espessura1)
    # ===========================================
    comprimento1 = corda1.altera_comprimento()
    corda1.set_comprimento(comprimento1)
    # ===========================================
    preco1 = corda1.aumenta_valor(aumenta_valores)
    # ===========================================
    corda1.mostra_dados()
#-----------------------------------------------------------------------------------------

    print('-=-' * 30)
    print('-> CORDA 2 <-')
    print('Digite as novas medidas para a corda 2: ')
# -----------------------------------------------------------------------------------------
    marca2 = corda2.altera_marca()
    corda2.set_marca(marca2)
    # ===========================================
    espessura2 = corda2.altera_espessura()
    corda2.set_espessura(espessura2)
    # ===========================================
    comprimento2 = corda2.altera_comprimento()
    corda2.set_comprimento(comprimento2)
    # ===========================================
    preco2 = corda2.aumenta_valor(aumenta_valores)
    # ===========================================
    corda2.mostra_dados()
# -----------------------------------------------------------------------------------------

    print('-=-' * 30)
    print('-> CORDA 3 <-')
    print('Digite as novas medidas para a corda 3: ')
# -----------------------------------------------------------------------------------------
    marca3 = corda3.altera_marca()
    corda3.set_marca(marca3)
    # ===========================================
    espessura3 = corda3.altera_espessura()
    corda3.set_espessura(espessura3)
    # ===========================================
    comprimento3 = corda3.altera_comprimento()
    corda3.set_comprimento(comprimento3)
    # ===========================================
    preco3 = corda3.aumenta_valor(aumenta_valores)
    # ===========================================
    corda3.mostra_dados()
# -----------------------------------------------------------------------------------------

    print('-=-' * 30)
    print('-> CORDA 4 <-')
    print('Digite as novas medidas para a corda 4: ')
# -----------------------------------------------------------------------------------------
    marca4 = corda4.altera_marca()
    corda4.set_marca(marca4)
    # ===========================================
    espessura4 = corda4.altera_espessura()
    corda4.set_espessura(espessura4)
    # ===========================================
    comprimento4 = corda4.altera_comprimento()
    corda4.set_comprimento(comprimento4)
    # ===========================================
    preco4 = corda4.aumenta_valor(aumenta_valores)
    # ===========================================
    corda4.mostra_dados()
# -----------------------------------------------------------------------------------------


