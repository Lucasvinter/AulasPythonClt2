# pip3 install flask
# pip3 install flask_mysqldb
# pip3 install flask_restful

from flask import Flask
from flask_restful import Api
from controllers.pessoa_controller import PessoaController

app = Flask(__name__)

api = Api(app)
api.add_resource(PessoaController, '/api/pessoa')

app.run()