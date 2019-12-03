#---- 1 - Cria uma app web com Flask
#---- 2 - Crie uma rota principal com:
#----   <h1> com nome da empresa
#----   <h2> com descricao da empresa
#----   <a> com link para a pagina de cadastro de pessoa
#---- 3 - Crie uma rota cadastro com:
#----   <form> para cadastro de pessoa
#----   <form> deve ter action para uma rota '/salvar'
#----   <form> deve ter method GET
#----   <form> deve ter 3 <input>
#----       1 - Nome Completo
#----       1 - RG
#----       1 - Idade

#----  Criar um link na pagina principal para a pagina de listagem de pessoas
#----  Criar um template contendo uma 'table' com as colunas correspondes de pessoa 


#--- Importação da biblioteca do Flask
from flask import Flask, render_template, request, redirect

#--- lista para armazenar as pessoas cadastradas
lista_pessoas = []

#--- Criação da variável através da classe Flask
app = Flask(__name__)

#--- Criar rota principal
@app.route('/')
def inicio():
    return render_template('home.html')

#--- Criar rota de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

#--- Rota para salvar pessoa
@app.route('/salvar')
def salvar():
    #--- carregando os parametros da url, 
    # que sao baseados no 'name' dos inputs que estao no 'form'
    nome = request.args['nome']
    rg = request.args['rg']
    idade = int(request.args['idade'])
    #--- criação de um dicionário para armazenar dados da pessoa
    pessoa = {'nome':nome, 'rg':rg, 'idade':idade}
    #--- Adiciona o dicionário da pessoa à lista
    lista_pessoas.append(pessoa)
    return redirect('/lista')

#--- Rota de listagem
@app.route('/lista')
def lista():
    return render_template('lista.html', lista = lista_pessoas)
#--- Executar o servidor Flask
app.run()

