import pymysql.cursors
from ex004_users import conexao

def cadastro_livro():
    con = conexao()
    cursor = con.cursor()

    try:
        titulo = str(input('Título do livro: '))
        autor = str(input('Autor do livro: '))

        sql="INSERT INTO tbl_estante (titulo, autor) VALUES (%s, %s)"
        cursor.execute(sql, (titulo, autor))

        con.commit()
        print('Livro cadastrado com sucesso')
    except pymysql.Error as e:
        con.rollback()
        print('Erro ao cadastrar', e)
    except TypeError as typerror:
        con.rollback()
        print('Erro de digitação', typerror)
    finally:
        con.close()
        cursor.close()

def delete_livro():
    con = conexao()
    cursor = con.cursor()

    try:
        titulo = str(input('Título do livro: '))

        sql="DELETE FROM tbl_estante WHERE titulo=(%s)"
        cursor.execute(sql, titulo)

        con.commit()
        print('Livro deletado com sucesso')
    except pymysql.Error as e:
        con.rollback()
        print('Erro ao deletar', e)
    except TypeError as typerror:
        con.rollback()
        print('Erro de digitação', typerror)
    finally:
        con.close()
        cursor.close()

def listar_all():
    con = conexao()
    cursor = con.cursor()

    try:
        sql = "SELECT * FROM tbl_estante"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
    finally:
        con.close()
        cursor.close()

def listar_some():
    con = conexao()
    cursor = con.cursor()
    sql = 0

    print('1 - Titulo / 2 - ID / 3 - Autor')
    enter = str(input('Opção de busca: '))
    if '1' in enter:
        titulo = str(input('Titulo: '))
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE titulo = (%s)'
        cursor.execute(sql, titulo)
    elif '2' in enter:
        id_ = str(input('ID: '))
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE id = (%s)'
        cursor.execute(sql, id_)
    else:
        autor = str(input('Autor: '))
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE autor = (%s)'
        cursor.execute(sql, autor)

    try:
        res = cursor.fetchall()
        print(res)
    finally:
        con.close()
        cursor.close()

