import random

def ler_alunos():
    with open('Sorteio/alunosbkp.txt','r') as arquivo:
        for a in arquivo:
            lista_alunos.append(a.strip())

def busca_nome_aluno(index):
    return lista_alunos[index]            

lista_alunos = []            
lista_sorteados = [14,10,8,13,2,4,5,12,9,3,1,7,6,11]
ler_alunos()

# for i in range(0,14):
#     sorteado =  random.randint(0,13)
#     while(lista_sorteados.count(sorteado) > 0):
#         sorteado =  random.randint(0,13)
#     lista_sorteados.append(sorteado)

print('='*50)
print('\n'*3)

lista_alunos_sorteados=[]
for i in range(0,13,2):
    lista_grupos = [busca_nome_aluno(lista_sorteados[i]-1), busca_nome_aluno(lista_sorteados[i+1]-1)]    
    lista_alunos_sorteados.append(lista_grupos)
for i in range(0,7):
    print(f' Grupo: {i+1} ')
    for ig in lista_alunos_sorteados[i]:
        print('{} {}'.format(' '*4 , ig))

print('\n'*3)
print('='*50)