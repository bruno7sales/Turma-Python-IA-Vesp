# Entrada de Dados
nome = input('Informe seu nome: ')
idade = int(input ('Informe sua idade: '))


# Executando Loop Infinito
while True:

    # Opções de Filme

    print('1 - Divertidademente (Classificação Livre!)')
    print('2 - Minions (Classificação Livre!)')
    print('3 - Deadpool and Wolverine (Faixa étria indicada: 16 anos).')
    print('4 - Titanic (Faixa étaria indicada: 12 anos)')
    print('5 - Operação Big Hero (Classificação Livre!)')

    opcao = input('\n Escolhe uma das seções acima! \n\n')

    # Switch...case
    match int(opcao):
        case 1:
            print(f'\nParabéns, {nome}, você escolheu: Divertidamente! O CineSenai te deseja uma ótima seção. ')

        case 2:
            print(f'\nParabéns, {nome}, você escolheu: Minions" o CineSenai te deseja uma ótima seção. ')

        case 3:
            if idade >= 16:
                print(f'\nParabéns, {nome}, você escolheu: Deadpool and Wolverine! O CineSenai te deseja uma ótima seção.')
            else:
                print(f'\n{nome}, infelizmente você não atende aos requisitos de idade para esse filme')

        case 4:
            if idade >= 12:
                print(f'\nParabéns, {nome}, você escolheu: Titanic! O CineSenai te deseja uma ótima seção.')
            else:
                print(f'\n{nome}, infelizmente você não atende aos requisitos de idade para esse filme')

        case 5:
            print(f'\nParabéns, {nome}, você escolheu: Operação Big Hero! o CineSenai te deseja uma ótima seção. ')

    # Verifica se p usúario deseja continuar
    continuar = input('Deseja continuar (s/n)').lower()

    # Verifica a opção do usúario
    if continuar == 's':
        continue
    else:
        break

