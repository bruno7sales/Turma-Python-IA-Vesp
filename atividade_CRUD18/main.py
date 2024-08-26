import os
nomes = []

while True:
    print('1 - Listar todos os nomes.')
    print('2 - Cadastrar novo nome.')
    print('3 - Pesquisar nome cadastrado.')
    print('4 - Alterar nome cadastrado.')
    print('5 - Excluir nome cadastrado.')
    print('0 - Encerrar programa.')

    opcao = input('Opção desejada: ')
    match opcao:
        case '1':
            for i in range(len(nomes)):
                print(f'Nome de indice {i}: {nomes[i]}.')
            continue
        case '2':
            novo_nome = input('Informe o novo nome: ')
            nomes.append(novo_nome)
            print(f'Nome "{novo_nome}" cadastrado com sucesso')
            continue
        case '3':
            nome_procurado = input("Informe o nome a pesquisar")
            contador = nomes.count(nome_procurado)
            print(f'{nome_procurado} foi encontrado {contador} vezes.')
            continue
        case '4':
            try:
                indice= int(input('Informe o indice a alterar: '))
                nomes[indice] = input('Informe o novo nome: ')
                print('Nome alterado com sucesso.')
            except:
                print('Não foi possível alterar o nome')
            finally: 
                continue
        case '5':
            try:
                indice = int(input('Informe o indice a excluir: '))
                del(nomes[indice])
                print('Nome excluido com sucesso.')
            except:
                print('Não foi possível excluir o número.')
            finally:
                continue
        case '0':
            print('Programa encerrado. Volte sempre!')
            break
        case _:
            print('Opção inválida')
            continue