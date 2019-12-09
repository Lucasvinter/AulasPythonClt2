from animal import Animal

class Mami(Animal):
    __tempo_gestacao = 0

    def get_tempo_gesta(self):
        return self.__tempo_gestacao
    def set_tempo_gesta(self, tempo):
        self.__tempo_gestacao = tempo


