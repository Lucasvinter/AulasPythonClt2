import MySQLdb

conn = MySQLdb.connect(host = 'mysql.topskills.study' ,database = 'topskills02' ,user = 'topskills02' ,passwd = 'Maykon2019')
cursor = conn.cursor()

def listar():
    cursor.execute('select * from local')
    lista = cursor.fetchall()    
    return lista

def buscar_por_id(id):
    cursor.execute(f'select * from local where id = {id}')
    item = cursor.fetchone()    
    return item

def inserir(nome):
    cursor.execute(f'insert into local( nome ) values("{nome}")')
    conn.commit()

def alterar(id, nome):
    cursor.execute(f'update local set nome = "{nome}" where id = {id}')
    conn.commit()

def deletar(id):
    cursor.execute(f'delete from local where id = {id}')
    conn.commit()

#inserir('Quero-Quero')
#alterar(7,'nâo tem café na sexta')
#deletar(14)

for l in listar():
    print(l)

