import pymysql.cursors

#Abrir uma conexão
def conexao():
    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        database='cadastro',
        password='',
        cursorclass=pymysql.cursors.DictCursor


    )

def consulta_cursos():
    conexao()

    with con.cursor() as c:
        sql = 'SELECT * FROM cursos'
        c.execute(sql)

        res = c.fetchall()
        for linha in res:
            print(f"ID: {linha['idcurso']} - Nome: {linha['nome']}")


def consulta_gafanhotos():
    conexao()

    with con.cursor() as c:
        sql = "SELECT * FROM gafanhotos"
        c.execute(sql)

        res = c.fetchall()
        for linha in res:
            print(f"ID: {linha['id']} - Nome: {linha['nome']}")

