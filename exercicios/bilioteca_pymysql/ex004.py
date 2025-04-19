import pymysql.cursors

def conexao():
    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='livraria',
        cursorclass=pymysql.cursors.DictCursor
    )

def cadastro_users():
    conexao()
    cursor = con.cursor()

    while True:
        try:
            nome = str(input('Nome: '))
            cpf = str(input('CPF: '))

            sql = "INSERT INTO tbl_users VALUES (%s, %s)"
            cursor.execute(sql, (cpf, nome))
            con.commit()
            print('Usuário cadastrado com sucesso')
        except pymysql.Error as mysqlerror:
            print('Erro ao cadastrar', mysqlerror)
            con.rollback()
        except TypeError as typerror:
            print('Erro de digitação', typerror)
            con.rollback()
            continue
        finally:
            cursor.close()
            con.close()
            break

def delete_user():
    conexao()
    cursor = con.cursor()

    while True:
        try:
            cpf = str(input('Deletar CPF: '))

            sql = "DELETE FROM tbl_users WHERE cpf = (%s)"
            cursor.execute(sql, cpf)
            con.commit()
            print('Usuário deletado com sucesso')
        except pymysql.Error as mysqlerror:
            print('Erro ao cadastrar', mysqlerror)
            con.rollback()
        except TypeError as typerror:
            print('Erro de digitação', typerror)
            con.rollback()
            continue
        finally:
            cursor.close()
            con.close()
            break

cadastro_users()


