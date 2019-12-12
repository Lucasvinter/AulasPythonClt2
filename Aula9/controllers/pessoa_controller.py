from flask_restful import Resource
from models.pessoa import Pessoa
from dao.pessoa_dao import PessoaDao

class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()
   
    def get(self):        
        return self.dao.lista_all()