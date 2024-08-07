# Executando Loop Infinito
while True:
    # Entrada de Dados
    x = str(input('Informe o primeiro numero: ')).replace (',', '.')
    y = str(input ('Informe o segundo numero: ')).replace (',', '.')

    x = float(x)
    y = float(y)

    # Opções de Operação Matematica:
    
    print('1 - Para multiplicação (X).')
    print('2 - Para Divisão (/).')
    print('3 - Para Subtração (-).')
    print('4 - Para Soma (+).')
    opcao = input('\n Escolha qual operação deseja realizar:\n')

    # Switch...case
    match int(opcao):
        case 1: print(x * y)
        case 2: print(x/y)
        case 3: print(x - y)
        case 4: print(x + y)
       

    #verifica se o usúario deseja continuar
    continuar = input('Deseja continuar (s/n)').lower()

    # Verifica a opção do usúario
    if continuar == 's':
        continue
    else:
        break
