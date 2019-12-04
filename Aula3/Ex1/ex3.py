from flask import Flask, render_template , redirect , request
from calc import *

app = Flask(__name__)

#--- Resolvido por Paloma teply variza
@app.route('/')
def inicio():
    return render_template('home.html')

#--- Resolvido por Isabel Christina Otte
@app.route('/resultado', methods=['POST'])
def resultado():
    resultado = {}
    numero1 = int(request.form['n1'])
    numero2 = int(request.form['n2'])

    resultado['soma'] = soma(numero1, numero2)
    resultado['subtracao'] = subtracao(numero1, numero2)
    resultado['multiplicacao'] = multiplicacao(numero1, numero2)
    resultado['divisao_inteira'] = divisao(numero1, numero2)
    resultado['divisao_fracionada'] = divisao_fracionada(numero1, numero2)
    resultado['raiz'] = f'{raiz(numero1, numero2):.2f}'

    return render_template('resultado.html',n1 = numero1, n2=numero2, resultados = resultado)

app.run(debug=True)

