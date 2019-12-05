from pessoa import Pessoa

class Cliente:
    #--- Método para cadastrar uma pessoa
    def cadastrar(self, pessoa:Pessoa):
        pessoa.id = self.gerar_id()
        with open('Aula3/Ex2/pessoa.txt', 'a') as arquivo:
            arquivo.write(f"{pessoa.id}; {pessoa.nome}; {pessoa.sobrenome}; {pessoa.cpf}\n")
    
    #--- Método para alterar uma pessoa --- Ainda não implementado 
    def alterar(self, pessoa_editada):
        lista_pessoas = self.listar()
        with open('Aula3/Ex2/pessoa.txt', 'w') as arquivo:
            arquivo.write('')
        for pessoa in lista_pessoas:
            if pessoa.id != pessoa_editada.id:
                self.cadastrar(pessoa)
            else:
                self.cadastrar(pessoa_editada)
    
    #--- Método para listar todas as pessoas cadastradas
    def listar(self):
        lista = []
        with open('Aula3/Ex2/pessoa.txt' , 'r') as arquivo:
            for linha in arquivo:
                dicLista = linha.strip().split(';')
                pessoa = Pessoa(dicLista[1],dicLista[2],dicLista[3],dicLista[0])
                lista.append(pessoa)
            return lista

    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar(self, id:int):
        lista_pessoas = self.listar()
        with open('Aula3/Ex2/pessoa.txt', 'w') as arquivo:
            arquivo.write('')
        for pessoa in lista_pessoas:
            if pessoa.id != id:
                self.cadastrar(pessoa)

    #--- Metodo para filtrar uma pessoa cadastrada pelo 'Id' recebido por parâmetro
    def buscar_id(self, id:int):
        with open('Aula3/Ex2/pessoa.txt', 'r') as arquivo:
            for l in arquivo:                
                dados = l.strip().split(';')
                if id in dados:
                    pessoa = Pessoa(dados[1], dados[2], dados[3] ,dados[0])
                    return pessoa
            return None

    #--- Método para filtrar por nome na lista de pessoas salvas
    def filtro_nome(self, nome):
        lista_resultados = []
        with open('Aula3/Ex2/pessoa.txt', 'a') as arquivo:
            for l in arquivo:
                dados = l.strip().split(';')
                if nome in dados:
                    pessoa = Pessoa(dados[1], dados[2], dados[3] ,dados[0])
                    lista_resultados.append(pessoa)
            return lista_resultados

    def gerar_id(self):
        id = 1
        with open('Aula3/Ex2/pessoa.txt', 'r') as arquivo:
            for linha in arquivo:
                dado = linha.strip().split(';')
                id = int(dado[0])+1
        return id
