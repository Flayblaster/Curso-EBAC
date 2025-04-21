def corretor_entradas(texto):
    """
    Trata a entrada de texto das variáveis na API
    entrada: Entrada de texto do usuário
    """
    while True:
        try:
            entrada = str(input(f'{texto}')).strip().title()
        except TypeError as e:
            print('Erro na digitação', e)
            continue
        finally:
            return entrada