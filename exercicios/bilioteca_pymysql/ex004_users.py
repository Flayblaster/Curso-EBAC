import pymysql.cursors
from ex004_treats import corretor_entradas

def conexao():
    """
    Faz a conexão do servidor do banco de dados com a API
    con: Variável que armazena a conexão
    """

    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='livraria',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con

def cadastro_users():
    """
    Faz o cadastro dos usuários novos, pedindo o CPF e Nome
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    nome: Entrada do Nome
    cpf: Entrada do CPF
    sql: Guarda o comando do banco de dados
    """

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
    """
    Deleta um usuario do banco de dados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    enter: Entrada da escolha do usuário
    """
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

def atualiza_users():
    """
    Atualiza informações de um usuários já cadastrado
    con: Armazena a conexão com o servidor
    enter: Entrada da escolha do usuário
    cursor: Metódo que executa os comandos no banco de dados
    sql: Guarda o comando do banco de dados
    nome_atual: Nome atual do usuário
    nome_novo: Nome novo do usuário
    cpf_atual: Cpf atual do usuário
    cpf_novo: Cpf novo do usuário
    """
    con = conexao()
    cursor = con.cursor()

    print('1 - Nome / 2 - CPF')
    enter = corretor_entradas('Opção de alteração: ')
    try:
        if '1' in enter:
            nome_atual = corretor_entradas('Nome atual: ')
            nome_novo = corretor_entradas('Nome novo: ')
            sql = 'UPDATE tbl_users SET nome = (%s) WHERE nome = (%s)'
            cursor.execute(sql, (nome_novo, nome_atual))
        else:
            cpf_atual = corretor_entradas('CPF atual: ')
            cpf_novo = corretor_entradas('CPF novo: ')
            sql = 'UPDATE tbl_users SET cpf =(%s) WHERE cpf = (%s)'
            cursor.execute(sql, (cpf_novo, cpf_atual))
        con.commit()
        print('Alteração feita com sucesso')
    except pymysql.Error as e:
        print('Erro de update', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()

def listar_users():
    """
    Lista todos os usuários cadastrados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    sql: Guarda o comando do banco de dados
    res: Resultado em um dict
    """
    con = conexao()
    cursor = con.cursor()

    try:
        sql = "SELECT * FROM tbl_users"
        cursor.execute(sql)
        res = cursor.fetchall()

        for coluna in res:
            print(f'Nome: {coluna["nome"]} /// CPF: {coluna["cpf"]}')
    finally:
        con.close()
        cursor.close()

def listar_user():
    """
    Lista alguns usuários específicos cadastrados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    enter: Guarda a entrada do usuário
    nome: Guarda o nome do usuário
    cpf: Guarda o cpf do usuário
    sql: Guarda o comando do banco de dados
    res: Resultado em um dict
    """
    con = conexao()
    cursor = con.cursor()
    try:
        print('1 - Nome / 2 - CPF')
        enter = corretor_entradas('Opção de busca: ')
        if '1' in enter:
            nome = corretor_entradas('Nome: ')
            sql = 'SELECT nome, cpf FROM tbl_users WHERE nome = (%s)'
            cursor.execute(sql, nome)
        else:
            cpf = corretor_entradas('CPF: ')
            sql = 'SELECT nome, cpf FROM tbl_users WHERE cpf = (%s)'
            cursor.execute(sql, cpf)

            res = cursor.fetchall()
            print(f'Nome: {res[0]['nome']} /// CPF: {res[0]['cpf']}')
            return res[0]['cpf']
    except pymysql.Error as e:
        print('Erro ao mostrar informações', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()