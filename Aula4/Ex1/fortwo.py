lista_terminal = ['Piloto','Oficial1', 'Oficial2', 'Chefe de Servico','Comissaria1','Comissaria2','Policial','Presidiario']
lista_aviao = []
viagem = 0

def imprime_cabecalho():
    print('='*50)
    print('\rA HBSIS Airlines','\n'*2)

def imprime_rodape():
    print('\n'*2)
    print('='*50)

def imprime_terminal_aviao():
    print('\033[1;30m')
    print(f'Pessoas que estão no terminal: {lista_terminal} ')    
    print(f'Pessoas que estão no aviao: {lista_aviao} ')
    print('\033[m')

def embarcar_fortwo(motorista, passageiro):
    global viagem
    viagem+=1
    print('\033[1;32m')
    print(f'\nViagem {viagem}\nIniciando o embarque no fortwo...')
    print('\033[m')
    lista_terminal.remove(passageiro)
    print(f'Realizando a viagem com o Fortwo: \033[2;20m motorista: {motorista} \033[m - passageiro: {passageiro}')
    embarcar_aviao(passageiro) 
    if(len(lista_terminal)!=1):
        print(f'{motorista} - Voltanto para o terminal')
        print(f'Chegada no terminal! {motorista} volta ao terminal')
    else:
        lista_aviao.append(lista_terminal[0])
        lista_terminal.remove(lista_terminal[0])

def embarcar_aviao(pessoa):
    print('Desenbarcando do Fortwo...')
    print(f'{pessoa} embarcando no aviao ...')
    lista_aviao.append(pessoa)

def realizar_viagem(motorista, passageiro):    
    embarcar_fortwo(motorista,passageiro)  
    imprime_terminal_aviao()