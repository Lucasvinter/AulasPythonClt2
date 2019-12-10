class Pessoa:
    nome = ''
    sobrenome = ''
    idade = 0

    def cadastrar(self):
        self.nome = input('Digite o seu nome: ')
        self.sobrenome = input('Digite o seu sobrenome: ')
        self.idade = int(input('Digite o seu idade: '))
        
    def format_pessoa(self):
        return f"{ self.nome };{self.sobrenome};{self.idade}"