import pymysql.cursors 

#abrir uma conexao a um banco de dados

conx = pymysql.connect (host='localhost', user='root', database='cadastro', password='', cursorclass=pymysql.cursors.DictCursor)

'''
'pymysql.cursors.DictCursor' é um parâmetro que faz o resultado ser mostrado em um dicionario, sendo os indices as colnas do banco de 
dados. Caso contrario será mostrado em tupla, sendo os indices numéricos
'''

#preparar  um cursor com o método .cursor()
with conx.cursor() as c:
    #Criar uma consulta 
    sql = "SELECT idcurso, nome, descricao FROM cursos"
    c.execute(sql)
    res = c.fetchone()
    print(res)
    print(f'Curso retornado: {res['nome']}')

    # Outra consulkta: dados da tabela de cursos
    sql = 'SELECT nomen FROM cursos'
    res = c.fetchall()
    print(res)
    print()
    for linha in res:
        print(linha['nome'])