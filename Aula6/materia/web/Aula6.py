#--- 09-12-2019
#--- 

from flask import Flask, render_template

lista = ['Csharp', 'Java', 'Cobol', 'Pytao']

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template( 'home.html', titulo='Minha paginazinha', lista=lista )

app.run(debug=True)