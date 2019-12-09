import MySQLdb
# import sys
# sys.path.append('BaseDao')

class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect('')
        self.cursor = self.conexao.cursor()

    def listar(self, comando_select):
        #self.cursor.execute(comando_select)
        pass

    def deletar(self):
        pass

    def inserir(self, comando_inserir):   
        print(comando_inserir)     
        #self.cursor.execute(comando_inserir)
        
    
    def alterar(self):
        pass
    def buscar_por_id(self):
        pass