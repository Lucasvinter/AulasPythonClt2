#----- Exercicio 3

#-- 1 - Criar uma aplicação# web com Flask
#-- 2 - Pagina Principal # com mensagem de boas-vindas
#-- 3 - Pagina principal com menu para modulo de produtos (Lista, Cadastro)
#-- 4 - Cadastro de produto Nome, Descrição, Valor
#-- 5 - Listagem deve ser feita em uma '<table>'
#-- 6 - Todas as páginas devem ter um cabeçalho

from flask import Flask, render_template, request, redirect
from files import ler_produtos,salvar_produto

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/listagem')
def listagem():
    return render_template('listagem.html', produtos = ler_produtos() )

@app.route('/salvar')
def salvar():
    lista_cadastro = {}

    nome = request.args['nome']
    descricao = request.args['descricao']
    valor = request.args['valor']

    lista_cadastro['nome']= nome
    lista_cadastro['descricao']= descricao
    lista_cadastro['valor']= valor

    salvar_produto(lista_cadastro)
    return redirect ('/listagem')





app.run(debug=True)