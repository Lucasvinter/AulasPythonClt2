from flask import Flask, render_template, request, redirect
from pessoa import Pessoa
from cliente import Cliente

app = Flask(__name__)

@app.route('/')
def listagem():
    opt = Cliente()
    paranaue = opt.listar()
    return render_template('listagem.html', paranaue = paranaue)

@app.route('/cadastrar')
def form_cadastrar():
    return render_template('formulario.html')

@app.route('/editar')    
def editar():
    id = request.args['id']
    cliente = Cliente()
    pessoa = cliente.buscar_id(id)
    return render_template('editar.html', pessoa = pessoa)

@app.route('/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    pessoa = Pessoa(nome, sobrenome, cpf)
    cliente = Cliente()
    cliente.cadastrar(pessoa)
    return redirect('/')

@app.route('/salvar_editar', methods=['POST'])
def editar_salvar():
    id = request.form['id']
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    pessoa = Pessoa(nome, sobrenome, cpf, id)
    cliente = Cliente()
    cliente.alterar(pessoa)
    return redirect('/')


app.run(port=80, debug=True)