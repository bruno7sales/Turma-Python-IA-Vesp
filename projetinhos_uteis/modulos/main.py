from cinematico import *
while True:
# Mostrar menu na tela
    mostra_menu()

    opcao = input('Opção de usuário: ')
    match opcao:
        case '1':
            m = float(input('Informe em kg: ').replace(',', '.'))
            h = float(input('Informe a altura em metros: ').replace(',', '.'))
            print(f'Energia potêncial: {calcular_ep(m, h):,.2f} J.')
        
            continue
        case '2':
            m = float(input('Informe o valor em kg: ').replace(',', '.'))
            v = float(input('Informe o valor em metros por segundo: ').replace(',', '.'))
            print(f'Energia cinetica: {calcular_ec(m, v):,.2f} J.')
            
            continue
        case '0':
            print('Progama encerrado.')
            break

