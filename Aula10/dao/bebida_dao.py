from base_dao import BaseDao
from model.bebida import Bebida
from model.tipo_bebida import TipoBebida

class BebidaDao(BaseDao):
    def inserir(self):
        comando_sql_insert = 
        super().inserir()


    def alterar(self):
        comando_sql_alterar = 
        super().inserir()
    
    def deletar(self):
        comando_sql_deletar = 
        super().inserir()

    def listar(self):
        lista_bebidas = []
        comando_sql_listar = """SELECT 
                                B.NOME
                                ,B.TEOR
                                ,TB.NOME
                                ,TB.DESCRICAO
                                ,TB.ID
                                ,B.ID
                                FROM BEBIDA_FESTA AS B
                                JOIN TIPO_BEBIDA AS TB
                                ON B.TIPO_BEBIDA_ID = TB.ID"""
                                
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            tipo_bebida = TipoBebida(l[2], l[3], l[4])
            bebida = Bebida( l[0], l[1], tipo_bebida, l[5] )
            lista_bebidas.append(bebida)
        return lista_bebidas



    def buscar_por_id(self):
        comando_sql_buscar_id = 
        super().inserir()