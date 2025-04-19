import pymysql.cursors

def conexao():
    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='cadastro',
        cursorclass=pymysql.cursors.DictCursor
    )


