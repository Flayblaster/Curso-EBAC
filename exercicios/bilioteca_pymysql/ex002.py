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

def cadastro_unico():
    nome = str(input("Nome: "))

    try:
        conexao()

        #Criar um cursor para executar a consulta
        cursor = con.cursor()

        #Inserir o registro na tabela usando consulta parametrizada
        sql = "INSERT INTO gafanhotos (nome) VALUES (%s)" # Usando a consulta parametrizada
        cursor.execute(sql, (nome))
        con.commit()

        print(f'O gafanhoto {nome} foi cadastro com sucesso')
    except pymysql.Error as e:
        print('Erro ao cadastrar curso', e)
        con.rollback()
    finally:
        cursor.close()
        con.close()
        print('Conexão encerrada')

def cadastro_mult():
    conexao()

    nome = str(input('Nome: '))
    carga = str(input('Carga horaria: '))
    id = 31
    try:
        cursor = con.cursor()
        sql = "INSERT INTO cursos (idcurso, nome, carga) VALUES (%s, %s, %s)"
        cursor.execute(sql, (id, nome, carga))
        con.commit()
        id += 1

        print(f"O curso {nome} foi adcionado com sucesso")
    except pymysql.Error as e:
        print('Erro ao cadastrar o curso', e)
        con.rollback()
    finally:
        cursor.close()
        con.close()
        print('Conexão encerrada')

cadastro_mult()