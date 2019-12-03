#-------- Aula 2 - Web 2

from flask import Flask, render_template

nome_aplicacao = 'CalcHb'

app = Flask(__name__)

@app.route('/')
def home():
    return 'S'

@app.route('/calc')
def calculadora():
    return render_template('calc.html', nome_app = nome_aplicacao )

app.run(host="0.0.0.0", port=80, debug=True)