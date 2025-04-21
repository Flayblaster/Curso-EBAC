from ex004_users import cadastro_users, delete_user, atualiza_users, listar_user, listar_users
from ex004_livros import cadastro_livro, delete_livro, atualiza_livros, listar_all, listar_some

def menu_inicial():
    """
    Gerencia todo a API, funciona como um menu, levando para toas as opções do sistema
    opc: Variavel que recebe as opções do usuários
    """

    while True:
        print('-'*20)
        print('{:^20}'.format('MENU'))
        print('{:^17}'.format('1 - LIVRARIA'))
        print('{:^17}'.format('2 - USUÁRIOS'))
        print('{:^17}'.format('3 - SAIR'))
        print('-'*20)

        opc = str(input('Opcão de navegação: '))
        if '1' in opc:
            menu_livraria()
        elif '2' in opc:
            menu_usuarios()
        else:
            break

def menu_usuarios():
    """
    Menu que gerencia a interface dos usuários
    opc: Guarda a opção do usuário
    """

    print('-' * 20)
    print('{:^20}'.format('MENU USUÁRIOS'))
    print('{:^17}'.format('1 - Cadastro de usuário'))
    print('{:^17}'.format('2 - Deletar usuário'))
    print('{:^17}'.format('3 - Editar usuário'))
    print('{:^17}'.format('4 - Ver algum usuário'))
    print('{:^17}'.format('5 - Ver todos usuário'))
    print('{:^17}'.format('6 - Voltar ao ínicio'))
    print('-' * 20)

    opc = str(input('Opcão de navegação: '))
    if '1' in opc:
        cadastro_users()
    elif '2' in opc:
        delete_user()
    elif '3' in opc:
        atualiza_users()
    elif '4' in opc:
        listar_user()
    elif '5' in opc:
        listar_users()
    else:
        menu_inicial()

def menu_livraria():
    """
    Menu que gerencia a interface da livraria
    opc: Guarda a opção do usuário
    """

    print('-' * 20)
    print('{:^20}'.format('MENU LIVRARIA'))
    print('{:^17}'.format('1 - Cadastrar livros'))
    print('{:^17}'.format('2 - Deletar livros'))
    print('{:^17}'.format('3 - Editar livros'))
    print('{:^15}'.format('4 - Ver todos livros'))
    print('{:^17}'.format('5 - Ver algum livros'))
    print('{:^17}'.format('6 - Voltar ao ínicio'))
    print('-' * 20)

    opc = str(input('Opcão de navegação: '))
    if '1' in opc:
        cadastro_livro()
    elif '2' in opc:
        delete_livro()
    elif '3' in opc:
        atualiza_livros()
    elif '4' in opc:
        listar_all()
    elif '5' in opc:
        listar_some()
    else:
        menu_inicial()

menu_inicial()