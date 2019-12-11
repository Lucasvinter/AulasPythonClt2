# O programador que trabalha com Java também conhece PostgreSql. 
# O framework de frontend de Nicole não é VUE. 
# O programador que usa Angular trabalha com MongoDb. 
# Mateus é especialista Python e não conhece MsSqlServer. 
# Tiago não sabe PHP. 


lista_programadores = ['Mateus', 'Tiago', 'Nicole']
lista_linguagem = ['Pyhon', 'PHP', 'Java']
lista_so = ['PostgreSql', 'MongoDb', 'MsSqlServer']
lista_ffe = ['React', 'Angular', 'Vue']


def removeg(dado):
    if dado in lista_programadores:
        lista_programadores.remove(dado)
def removem(dado):
    if dado in lista_linguagem:
        lista_linguagem.remove(dado)
def removes(dado):
    if dado in lista_so:
        lista_so.remove(dado)
def removec(dado):
    if dado in lista_ffe:
        lista_ffe.remove(dado)

def listag1(dado,p):
    lista1[p] = dado
def listag2(dado,p):
    lista2[p] = dado
def listag3(dado,p):
    lista3[p] = dado

lista1 = ['','','','']
lista2 = ['','','','']
lista3 = ['','','','']
# g, m, s, c
lista1[0] = lista_programadores[0]
lista2[0] = lista_programadores[1]
lista3[0] = lista_programadores[2]

for g in lista_programadores:
    for m in lista_linguagem:
        for s in lista_so:
            for c in lista_ffe:
                if(g == 'Mateus' and m =='Pyhon' and s== 'MongoDb' and c =='Angular'):                  
                    listag1(m,1)
                    listag1(s,2)
                    listag1(c,3)
                    removem(m)
                    removes(s)
                    removec(c)
                if(g == 'Tiago' and m =="Java" and s== 'PostgreSql' and c =='Vue'):
                    listag2(m,1)
                    listag2(s,2)
                    listag2(c,3)
                    removem(m)
                    removes(s)
                    removec(c)
                if(g == 'Nicole'and m =='PHP'  and s=='MsSqlServer' and c =='React' ):                    
                    listag3(m,1)   
                    listag3(s,2)                    
                    listag3(c,3)
                    removem(m)
                    removes(s)
                    removec(c)
                    
            
print(lista1)
print(lista2)
print(lista3,'\n')
print(lista_programadores)
print(lista_linguagem)
print(lista_so)
print(lista_ffe)