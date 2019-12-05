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

    calc = Calculadora(numero1, numero2)

    resultado['soma'] = calc.soma()
    resultado['subtracao'] = calc.subtracao()
    resultado['multiplicacao'] = calc.multiplicacao()
    resultado['divisao_inteira'] = calc.divisao()
    resultado['divisao_fracionada'] = calc.divisao_fracionada()
    resultado['raiz'] = f'{calc.raiz():.2f}'

    return render_template('resultado.html',n1 = calc.n1, n2=calc.n2, resultados = resultado)

app.run(debug=True)

