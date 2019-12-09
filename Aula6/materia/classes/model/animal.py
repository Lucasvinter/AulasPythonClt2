class Animal:       
    __nome_cientifico = ''
    __habitat = ''
    __tipo_alimentacao = ''

    def get_nome_cientifico(self):
        return self.__nome_cientifico
    def set_nome_cientifico(self,nome_cientifico):
        self.__nome_cientifico = nome_cientifico

    def get_habitat(self):
        return self.__habitat
    def set_habitat(self,habitat):
        self.__habitat = habitat

    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo = tipo



