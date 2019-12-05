#--- Resolvido por Cahik de Matos Soares
class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def soma(self):
        return self.n1 + self.n2

    def subtracao(self):
        return self.n1 - self.n2

    def divisao(self):
        return self.n1 // self.n2

    def multiplicacao(self):
        return self.n1 * self.n2

    def raiz(self):
        return self.n1 ** (1/self.n2)

    def divisao_fracionada(self):
       return self.n1 / self.n2