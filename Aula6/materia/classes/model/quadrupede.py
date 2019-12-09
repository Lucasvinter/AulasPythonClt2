from mami import Mami

class Quadrupede(Mami):
    __velocidade = 0

    def __init__(self, velocidade):
        self.__velocidade = velocidade

    def get_velocidade(self):
        return self.__velocidade 


