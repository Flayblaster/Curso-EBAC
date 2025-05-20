import pymysql.cursors
from ex004_users import conexao
from ex004_treats import corretor_entradas

def cadastro_livro():
    """
    Faz o cadastro dos livros novos, pedindo o Título e Nome do autor
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    titulo: Entrada do Título
    autor: Entrada do Autor
    sql: Guarda o comando do banco de dados
    """
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
    """
    Deleta um livro do banco de dados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    enter: Entrada da escolha do usuário
    titulo: Entrada do Título
    autor: Entrada do Autor
    sql: Comando que vai ser executado no banco de dados
    """

    con = conexao()
    cursor = con.cursor()

    print('1 - Titulo / 2 - Autor')
    enter = corretor_entradas('Opção de exclusão: ')
    try:
        if '1' in enter:
            titulo = corretor_entradas('Titulo: ')
            sql = 'DELETE FROM tbl_estante WHERE titulo=(%s)'
            cursor.execute(sql, titulo)
        else:
            autor = corretor_entradas('Autor: ')
            sql = 'DELETE FROM tbl_estante WHERE autor=(%s)'
            cursor.execute(sql, autor)
        con.commit()
        print('Alteração feita com sucesso')
    except pymysql.Error as e:
        print('Erro de exclusão', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()

def listar_all():
    """
    Lista todos os livros cadastrados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    sql: Guarda o comando do banco de dados
    res: Resultado em um dict
    """
    con = conexao()
    cursor = con.cursor()

    try:
        sql = "SELECT * FROM tbl_estante"
        cursor.execute(sql)
        res = cursor.fetchall()

        for coluna in res:
            print(f'Título: {coluna["titulo"]} /// Autor: {coluna["autor"]} /// ID: {coluna["id"]}')
    finally:
        con.close()
        cursor.close()

def listar_some():
    """
    Lista alguns livros específicos cadastrados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    enter: Guarda a entrada do usuário
    titulo: Guarda o titulo
    id_: Guarda o id do livro
    autor: Guarda o autor do livro
    sql: Guarda o comando do banco de dados
    res: Resultado em um dict
    """
    con = conexao()
    cursor = con.cursor()

    print('1 - Titulo / 2 - ID / 3 - Autor')
    enter = corretor_entradas('Opção de busca: ')
    if '1' in enter:
        titulo = corretor_entradas('Titulo: ')
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE titulo = (%s)'
        cursor.execute(sql, titulo)
    elif '2' in enter:
        id_ = corretor_entradas('ID: ')
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE id = (%s)'
        cursor.execute(sql, id_)
    else:
        autor = corretor_entradas('Autor: ')
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE autor = (%s)'
        cursor.execute(sql, autor)

    try:
        res = cursor.fetchall()
        print(f'Título: {res[0]['titulo']} /// Autor: {res[0]['autor']} /// ID: {res[0]['id']}')
        return res[0]['id']
    finally:
        con.close()
        cursor.close()

def atualiza_livros():
    """
    Atualiza informações de um livro já cadastrado
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    sql: Guarda o comando do banco de dados
    titulo_atual: Titulo atual do livro
    titulo_novo: Titulo novo do livro
    autor_atual: Autor atual do livro
    autor_novo: Autor novo do livro
    """

    con = conexao()
    cursor = con.cursor()

    print('1 - Titulo / 2 - Autor')
    enter = corretor_entradas('Opção de alteração: ')
    try:
        if '1' in enter:
            titulo_atual = corretor_entradas('Titulo atual: ')
            titulo_novo = corretor_entradas('Titulo novo: ')
            sql = 'UPDATE tbl_estante SET titulo = (%s) WHERE titulo = (%s)'
            cursor.execute(sql, (titulo_novo, titulo_atual))
        else:
            autor_atual = corretor_entradas('Autor atual: ')
            autor_novo = corretor_entradas('Autor novo: ')
            sql = 'UPDATE tbl_estante SET autor =(%s) WHERE autor = (%s)'
            cursor.execute(sql, (autor_novo, autor_atual))
        con.commit()
        print('Alteração feita com sucesso')
    except pymysql.Error as e:
        print('Erro de update', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()


