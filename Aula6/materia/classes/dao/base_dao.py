import MySQLdb

class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(host = 'mysql.topskills.study' ,database = 'topskills02' ,user = 'topskills02' ,passwd = 'Maykon2019')
        self.cursor = self.conexao.cursor()

    def listar(self, comando_select):
        pass

    def deletar(self, comando_deletar):
        pass

    def inserir(self, comando_inserir):   
        print(comando_inserir)             
    
    def alterar(self, comando_alterar):
        pass

    def buscar_por_id(self, comando_buscar_por_id):
        pass