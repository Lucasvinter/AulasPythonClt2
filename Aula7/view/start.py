import sys
sys.path.append("C:/Users/mayko/OneDrive/Área de Trabalho/Teste/")
from model.pessoa import Pessoa
from dao.pessoa_dao import PessoaDao

dao = PessoaDao()

for i in range(0,2):
    pessoa = Pessoa()
    pessoa.cadastrar()
    dao.salvar(pessoa)

dao.ler()