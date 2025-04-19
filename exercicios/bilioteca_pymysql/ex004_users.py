import pymysql.cursors
from ex004_treats import corretor_entradas

def conexao():
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='livraria',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con

def cadastro_users():
    con = conexao()
    cursor = con.cursor()

    while True:
        try:
            nome = corretor_entradas('Nome: ')
            cpf = corretor_entradas('CPF: ')

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
    con = conexao()
    cursor = con.cursor()

    print('1 - Nome / 2 - CPF')
    enter = corretor_entradas('Opção de exclusão: ')
    try:
        if '1' in enter:
            nome = corretor_entradas('Nome: ')
            sql = 'DELETE FROM tbl_users WHERE nome=(%s)'
            cursor.execute(sql, nome)
        else:
            cpf = corretor_entradas('CPF: ')
            sql = 'DELETE FROM tbl_users WHERE cpf=(%s)'
            cursor.execute(sql, cpf)
        con.commit()
        print('Alteração feita com sucesso')
    except pymysql.Error as e:
        print('Erro de exclusão', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()
