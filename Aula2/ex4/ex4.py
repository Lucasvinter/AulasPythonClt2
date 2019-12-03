#--- Crie um arquivo python que contenha duas funções
#--- 1 - Função de salvar um dicionario em arquivo texto
#--- 2 - Função que leia o arquivo texto e converta cada linha em um dicionário
#---     esta função deve retornar a lista de dicionários
#--- Testar as funções criando um aplicação no terminal
#--- Terminal deve ler nome da cerveja, teor, tipo

def salvar_dicionario(cervejas):
    with open('Aula2/ex4/cervejas.txt','a') as arquivo:
        arquivo.write(f'{ cervejas["nome"] };{ cervejas["teor"] };{ cervejas["tipo"] }\n')

def ler_arquivo():
    lista = []
    with open('Aula2/ex4/cervejas.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.strip().split(';')
            lista.append({'nome': linha[0], 'teor': linha[1], 'tipo': linha[2]})
    return lista
