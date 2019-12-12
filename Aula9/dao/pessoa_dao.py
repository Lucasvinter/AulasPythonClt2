import MySQLdb
from models.pessoa import Pessoa
class PessoaDao:
    def lista_all(self):
        lista_pessoas = []
        connec =MySQLdb.connect(host="mysql.topskills.study",database="topskills02", user="topskills02", passwd="Maykon2019")
        cursor  = connec.cursor()
        cursor.execute("SELECT Nome, Sobrenome, Id FROM Pessoa")
        for p in cursor.fetchall():
            pessoa = Pessoa(p[0], p[1], p[2])
            lista_pessoas.append(pessoa.__dict__)
        return lista_pessoas
