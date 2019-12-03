from flask import Flask, render_template, redirect, request

app = Flask(__name__)
nome_app = 'Cervas'

lista_cerva = ['Skol', 'Brahma', 'Corona', 'Bud', 'Original']

@app.route('/')
def inicio():
    return render_template('home.html', nome = nome_app, lista = lista_cerva)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/salvar')
def salvar():
    nome = request.args['nome']
    lista_cerva.append(nome)
    return redirect('/')

app.run()