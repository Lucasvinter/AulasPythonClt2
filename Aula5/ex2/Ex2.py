#1. A menina que gosta de português gosta de suco de abacaxi.
#2. A mochila de Manuela não é laranja.
#3. A garota da mochila vermelha gosta de suco de limão.
#4. Aline gosta de história e não gosta de suco de uva.
#5. Flávia não gosta de matemática.


lista_programadores = ['Aline', 'Flavia', 'Manuela']
lista_linguagem = ['Pyhon', 'PHP', 'Java']
lista_so = ['Linux', 'Macos', 'Windows']
lista_ide = ['React', 'Angular', 'Vue']

#menina que  gosta de portugues, gosta de abacaxi
#manoela não laranja
#mochila vermelha suco de limao
#aline historia nao uva
#flavia matemática
def removeg(dado):
    if dado in lista_g:
        lista_g.remove(dado)
def removem(dado):
    if dado in lista_m:
        lista_m.remove(dado)
def removes(dado):
    if dado in lista_s:
        lista_s.remove(dado)
def removec(dado):
    if dado in lista_c:
        lista_c.remove(dado)

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
lista1[0] = lista_g[0]
lista2[0] = lista_g[1]
lista3[0] = lista_g[2]

for g in lista_g:
    for m in lista_m:
        for s in lista_s:
            for c in lista_c:
                if(g == 'Aline' and m =='Historia' and s== 'Limao' and c =='Vermelha'):                  
                    listag1(m,1)
                    listag1(s,2)
                    listag1(c,3)
                    removem(m)
                    removes(s)
                    removec(c)
                if(g == 'Flavia' and m =="Portugues" and s== 'Abacaxi' and c =='Laranja'):
                    listag2(m,1)
                    listag2(s,2)
                    listag2(c,3)
                    removem(m)
                    removes(s)
                    removec(c)
                if(g == 'Manuela'and m =='Matematica'  and s=='Uva' and c =='Rosa' ):                    
                    listag3(m,1)   
                    listag3(s,2)                    
                    listag3(c,3)
                    removem(m)
                    removes(s)
                    removec(c)
                    
            
print(lista1)
print(lista2)
print(lista3,'\n')
print(lista_g)
print(lista_m)
print(lista_s)
print(lista_c)