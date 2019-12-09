# 1- A tripulação técnica é constituída pelo 
#     piloto
#     oficial1
#     oficial2

# 2- A tripulação de cabine é constituída pelo 
#     chefe de serviço de voo
#     comissária1
#     comissária2
    
# 3 - Dirigir:
#     piloto
#     chefe de serviço 
#     policial

# 4 - nenhum dos oficiais pode ficar sozinho com o chefe de serviço
# 5 - nenhuma das comissárias pode ficar sozinha com o piloto.  

# 6 - Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. 



from yuri2 import SmartFortwo

terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de serviço', 'Comissaria 1', 'Comissaria 2', 'Policial', 'Prisioneiro']
aviao =[]

smart_fortwo = SmartFortwo(terminal, aviao)

smart_fortwo.viagem_terminal_aviao('Piloto', 'Oficial 1')
smart_fortwo.viagem_aviao_terminal('Piloto')

smart_fortwo.viagem_terminal_aviao('Piloto', 'Oficial 2')
smart_fortwo.viagem_aviao_terminal('Piloto')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Comissaria 1')
smart_fortwo.viagem_aviao_terminal('Chefe de serviço')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Comissaria 2')
smart_fortwo.viagem_aviao_terminal('Chefe de serviço')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Piloto')
smart_fortwo.viagem_aviao_terminal('Chefe de serviço')

smart_fortwo.viagem_terminal_aviao('Policial', 'Prisioneiro')
smart_fortwo.viagem_aviao_terminal('Piloto')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Piloto')

smart_fortwo.mostra_situacao()