#--- Provinha 1

#--- 1 -Criar aplicação web utilizando Flask
#--- 2 - Criar uma rota principal que retorne uma string com nome da 'Firma'
#--- 3 - Criar uma rota para carregar pagina de template 'Sobre'

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def joelma():
    return 'Calypso'

@app.route('/sobre')
def chimbinha():
    return render_template('sobre.html')

app.run()