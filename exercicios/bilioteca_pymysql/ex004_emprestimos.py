import pymysql.cursors
from ex004_users import conexao
from ex004_livros import listar_some
from datetime import date
from ex004_users import listar_user

def emprestimo():
    """
    Sistema de emprestimos, mas incompleto ainda
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    id_livro: Id do livro que vai ser pego ou devolvido
    id_user: Id do usuário que vai pegar ou devolver um livro
    data_emprestimo: Data da cautela
    sql: Comando que vai ser executado no banco de dados
    """
    con = conexao()
    cursor = con.cursor()
    try:
        id_livro = listar_some()
        id_user = listar_user()
        data_emprestimo = date.today()
        sql = "INSERT INTO tbl_emprestimos (livro_id, usuario_id, data_emprestimo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (id_livro, id_user, data_emprestimo))

        con.commit()
        print('Empréstimo cadastrado')
    except pymysql.Error as e:
        print('Erro no emprestimo', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()

emprestimo()