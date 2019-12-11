import random
arquivo = 'C:/Dados/Git/Python/AulasPythonClt2/Sorteio/grupos_sorteados.txt'
def salva(sorteado):
    with open(arquivo,'a') as arq:
        arq.write(f'{sorteado}\n')
        
def valida(sorteado):
    with open(arquivo, 'r') as arq:
        for l in arq:
            ng = int(l.strip())
            if(sorteado==ng):
                return True
        return False

sortear = True
sorteado = 0
while(sortear):
    sorteado = int( random.randint(1,7) )
    sortear = valida(sorteado)
salva(sorteado)
print(f'Grupo - {sorteado}')