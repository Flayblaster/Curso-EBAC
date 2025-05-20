import pymysql.cursors
from pymysql.connections import Connection


#Abrir uma conexão
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


def consulta_cursos():
    """
    Faz uma consulta no bancos de dados: 'cursos'
    """
    
    conexao()
    with con.cursor() as c:
        sql = 'SELECT * FROM cursos'
        c.execute(sql)

        res = c.fetchall()
        for linha in res:
            print(f"ID: {linha['idcurso']} - Nome: {linha['nome']}")


def consulta_gafanhotos():
    """
    Faz uma consulta ao banco de dados: 'gafanhotos'
    """

    conexao()
    with con.cursor() as c:
        sql = "SELECT * FROM gafanhotos"
        c.execute(sql)

        res = c.fetchall()
        for linha in res:
            print(f"ID: {linha['id']} - Nome: {linha['nome']}")


def cadastro_unico():
    """
    Faz o cadastro de uma única informação por vez
    """

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
    """
    Faz o cadastro de várias informações de uma vez só. Em outros termos, 
    ele cadastra várias informações de um indivíduo.
    """
    
    conexao()
    cursor = con.cursor()
    
    nome = str(input('Nome: '))
    carga = str(input('Carga horaria: '))
    id = 31

    try:
        sql = "INSERT INTO cursos (idcurso, nome, carga) VALUES (%s, %s, %s)"
        cursor.execute(sql, (id, nome, carga))
        id += 1

        con.commit()
        print(f"O curso {nome} foi adcionado com sucesso")
    except pymysql.Error as e:
        print('Erro ao cadastrar o curso', e)
        con.rollback()
    finally:
        cursor.close()
        con.close()
        print('Conexão encerrada')


def cadastro_many():
    """
    Faz o cadastro de muitas linhas ao mesmo tempo, usando o método: .executemany()
    """
    
    conexao()
    cursor = con.cursor()

    nome1 = str(input('Digite o primeiro nome: '))
    nome2 = str(input('Digite o segundo nome: '))
    nome3 = str(input('Digite o terceiro nome: '))
    nomes = (nome1, nome2, nome3)

    try:
        sql = "INSERT INTO gafanhotos (nome) VALUES (%s)"
        cursor.executemany(sql, (nomes))
        
        con.commit()
        print(f'Os nomes {nomes} foram cadastrados com sucesso!!')
    except pymysql.Error as e:
        print("Ocorreu um erro:", e)
        con.rollback()
    finally:
        cursor.close()
        con.close()
        print('Conexão encerrada') 


def cadastro_mult_many():
    """
    Faz o cadastro de vários indivíduos e vários informações sobre eles.
    """
    
    conexao()
    cursor = con.cursor()

    nome_1 = str(input("Nome da primeira pessoa: "))
    nacionalidade_1 = str(input("Nacionalidade da primeira pessoa: "))
    nome_2 = str(input('Nome da segunda pessoa: '))
    nacionalidade_2 = str(input("Nacionalidade da segunda pessoa: "))
    pessoas = ([nome_1, nacionalidade_1], [nome_2, nacionalidade_2])

    try:
        sql = "INSERT INTO gafanhotos (nome, nacionalidade) VALUES (%s, %s)"
        cursor.executemany(sql, (pessoas))
        
        con.commit()
        print('Cadastro feito com sucesso')
    except pymysql.Error as e:
        print('Erro ao cadastrar:', e)
        con.rollback()
    finally:
        cursor.close()
        con.close()
        print('conexão encerrada')
