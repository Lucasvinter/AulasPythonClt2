def salvar_produto(produto):
    with open('Aula2/ex3/produtos.txt','a') as arquivo:
        arquivo.write(f'{ produto["nome"] };{ produto["descricao"] };{ produto["valor"] }\n')

def ler_produtos():
    lista = []
    with open('Aula2/ex3/produtos.txt','r') as arquivo:
        for linha in arquivo:
            produtoLista = linha.strip().split(';')
            produto = {'nome': produtoLista[0] , 'descricao': produtoLista[1], 'valor': produtoLista[2]}
            lista.append(produto)
    return lista