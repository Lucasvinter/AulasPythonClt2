from ex4 import ler_arquivo, salvar_dicionario

nome = input('Nome: ')
teor = input('Teor: ')
tipo = input('Tipo: ')

cerveja = {'nome' : nome, 'teor' : teor, 'tipo' : tipo}
salvar_dicionario(cerveja)
lista = ler_arquivo()

print(lista[len(lista)-1])