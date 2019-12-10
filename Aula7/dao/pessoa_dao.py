from model.pessoa import Pessoa

class PessoaDao:
    def salvar(self, pessoa:Pessoa):
        with open('dao/pessoa.txt', 'a') as arquivo:
            arquivo.write(pessoa.format_pessoa()+'\n')

    def ler(self):
        with open('dao/pessoa.txt','r') as arquivo:
            for l in arquivo:
                lista_dados = l.strip().split(';')
                pessoa =  Pessoa()
                pessoa.nome = lista_dados[0]
                pessoa.sobrenome = lista_dados[1]
                pessoa.idade = lista_dados[2]
                print(pessoa.format_pessoa())