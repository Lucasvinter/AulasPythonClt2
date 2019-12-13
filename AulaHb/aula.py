class Teste:
    nome = ''
t = Teste()
t2 = Teste()

print(id(t))
print(id(t2))

t2 = t
print(id(t))
print(id(t2))

numero = 10.50
print (id(numero))
numero = 12.50
print (id(numero))
numero = "asd"
print(id(numero))

