import pymysql.cursors
from ex002 import consulta_gafanhotos


def conexao():
    """
    Gera a conexão com o banco de dados
    """

    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        database='cadastro',
        password='',
        cursorclass=pymysql.cursors.DictCursor
    )


def altera():
    conexao()
    cursor = con.cursor()

    try:
        nome_atual = str(input('Nome atual do gafanhoto: '))
        nome_novo = str(input('Novo nome do gafanhoto: '))
        valores = (nome_novo, nome_atual)

        sql = "UPDATE gafanhotos SET nome = %s WHERE nome = %s LIMIT 1;"
        cursor.execute(sql, valores)

        con.commit()
        print('Alteração feita com sucesso')
    except pymysql.Error as e:
        con.rollback()
        print('Erro no cadastro', e)
    finally:
        con.close()
        cursor.close()
        print('Conexão encerrada')

def delete():
    conexao()
    cursor = con.cursor()

    try:
        id = str(input('Id do gafanho a ser excluido: '))

        sql = "DELETE FROM gafanhotos WHERE id = (%s)"
        cursor.execute(sql, id)

        con.commit()
        print('Registro deletado com sucesso')
    except pymysql.Error as e:
        print('Erro ao deletar o registro', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()
        print('Conexão fechada')

delete()
consulta_gafanhotos()