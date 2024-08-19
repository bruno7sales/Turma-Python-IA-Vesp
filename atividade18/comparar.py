# Definindo as chaves para o cadastro de usuários
chaves = ('Nome', 'Data de Nascimento', 'CPF', 'Profissão', 'E-mail', 'Endereço', 'Telefone')

# Lista para armazenar os dados dos usuários
usuarios = []

while True:
    print(f'{"=" * 50}\n')
    print('1 - Cadastrar usuário')
    print('2 - Exibir usuários')
    print('3 - Pesquisar por um usuário')
    print('4 - Alterar os dados do usuário')
    print('5 - Excluir usuário')
    print('0 - Encerrar Programa')
    print(f'{"=" * 50}\n')

    opcao = input('Opção do usuário: ')
    print(f'{"=" * 50}\n')

    match opcao:
        case '1':
            # Cadastrar usuário
            usuario = {}
            for chave in chaves:
                usuario[chave] = input(f'Informe o/a {chave}: ')
            usuarios.append(usuario)
            print(f'\nUsuário cadastrado com sucesso!\n')

        case '2':
            # Exibir usuários
            if not usuarios:
                print('Nenhum usuário cadastrado.')
            else:
                print(f'{"=" * 10} LISTA DE USUÁRIOS {"=" * 10}\n')
                index = 1
                for usuario in usuarios:
                    print(f'Usuário {index}:')
                    for chave in chaves:
                        print(f'{chave}: {usuario[chave]}')
                    print()
                    index += 1
                print(f'{"=" * 10}\n')

        case '3':
            # Pesquisar usuário
            nome = input('Informe o nome do usuário que deseja pesquisar: ')
            encontrado = False
            for usuario in usuarios:
                if usuario['Nome'].lower() == nome.lower():
                    print(f'\nUsuário encontrado:')
                    for chave in chaves:
                        print(f'{chave}: {usuario[chave]}')
                    print()
                    encontrado = True
                    break
            if not encontrado:
                print('Usuário não encontrado.')

        case '4':
            # Alterar dados do usuário
            nome = input('Informe o nome do usuário que deseja alterar: ')
            encontrado = False
            for usuario in usuarios:
                if usuario['Nome'].lower() == nome.lower():
                    print(f'\nUsuário encontrado. Informe os novos dados:')
                    for chave in chaves:
                        novo_dado = input(f'{chave} ({usuario[chave]}): ')
                        if novo_dado:
                            usuario[chave] = novo_dado
                    print('Dados do usuário atualizados com sucesso!\n')
                    encontrado = True
                    break
            if not encontrado:
                print('Usuário não encontrado.')

        case '5':
            # Excluir usuário
            nome = input('Informe o nome do usuário que deseja excluir: ')
            usuarios = [usuario for usuario in usuarios if usuario['Nome'].lower() != nome.lower()]
            print('Usuário excluído com sucesso!\n')

        case '0':
            # Encerrar Programa
            print('Programa encerrado.')
            break

        case _:
            # Opção inválida
            print('Opção inválida!')
