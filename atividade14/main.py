alunos = []
aluno_codigos = []

while True:
    print('1 - Inserir novo aluno. ')
    print('2 - Exibir lista de alunos.')
    print('3 - Atribuir nota ao aluno(a).')
    print('0 - Encerrar Progama.')


    #Opção do usuário
    opcao = input('Opção do usuário: ')

    #Verifica a opção escolhida
    match opcao:
        # inserindo novo aluno na lista
        case '1':
         aluno_novo = input('Insira o nome do(a) aluno(a): ')
         aluno_codigo_novo = int(input('Inforne o codigo de aluno: '))
         aluno_codigos.insert(aluno_codigo,aluno_novo)
         alunos.insert(aluno_codigo_novo, aluno_novo)
         alunos.sort()
         for aluno_codigo in aluno_codigos:
            print(f'')         
         continue
        # Exibindo lista de alunos
        case '2':
            print('\n LISTA DE ALUNOS: ')
            for aluno in alunos:
                print(f'{aluno_codigo} - {aluno}\n')
                continue
        # Exibindo menu de adição de notas
        case '3':
            print(f'')
          
        case '0':
          print('Progama encerrado.')
          break
        case _:
          print('Opção invalida!')

