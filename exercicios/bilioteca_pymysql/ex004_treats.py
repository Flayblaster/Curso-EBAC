def corretor_entradas(texto):
    while True:
        try:
            entrada = str(input(f'{texto}')).strip().title()
        except TypeError as e:
            print('Erro na digitação', e)
            continue
        finally:
            return entrada