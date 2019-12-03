# banda = input('Digite sua banda: ')
# valor = float(input('Digite valor disco: '))
dado = input('Digite um dado: ')
if(not dado):
    print('Nao tem dado')
#elif(type(dado) is int):
elif(dado.isnumeric()):
    print('Numbro')
elif(dado.isdigit()):
    print('Numbro com vrigula')
else:       
    print('Tem dado')


#print(valor)