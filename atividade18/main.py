chaves = ('Nome', 'Data de Nascimento', 'CPF', 'Profissão', 'E-mail', 'Endereço', 'Telefone')

usuarios = []

while True:
    print(f'{'=' * 50}\n')
    print('1 - Cadastrar usuário ')
    print('2 - Exibir usuários.')
    print('3 - Pesquisar por um usuário.')
    print('4 - Alterar os dados do usuário')
    print('5 - Excluir usuário')
    print('0 - Encerrar Progama.')


    #Opção do usuário
    opcao = input('Opção do usuário: ')
    print(f'{'=' * 50}\n')

    #Verifica a opção escolhida
    
    match opcao:
        
        case '1':
            usuario = {}
            for chave in chaves:
                usuario[chave] = input(f'Informe o/a {chave}: ')
            usuarios.append(usuario)
            print(f'\nUsuário cadastrado com sucesso!')
            print('\n')

            continue

        case '2':
            print(f'{'=' * 10} LISTA DE USUÁRIOS{'='*10}\n')
            contador = 1
            for usuario in usuarios:
                print(f'Usuário {contador}')
                for chave in chaves:
                 print(f'{chave}: {usuario[chave]}')
            print()
            contador += 1
            print(f'\n{'='*10}\n')
            
            continue
       
        case '3':
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
             continue
        
        case '4':
            print('\n')
            try:
             chaves = int(input('Informe o numero do usuario: '))
             contador[chaves] = input('Informe os novos dados: ').capitalize()
            except:
               print('Não possivel fazer a alteração!')
            print('\n')
            # Exibe a nova lista
            for i in range(len(contador)):
                print(f'Indicei {i}: {contador[i]}.')
        
       
        case '0':
          print('Progama encerrado.')
          break
        case _:
          print('Opção invalida!')

