# Executando Loop Infinito
while True:
    # Entrada de Dados
    print('Bem Vindo(a) a sua calculadora de IMC!')
    nome = input('Informe seu nome: ')
    peso= str(input ('Informe seu peso (em kg): ')).replace (',', '.')
    altura= str(input('Informe sua altura em metros: ')).replace (',', '.')
    altura =  float(altura)
    peso = float(peso)

    calculo = peso/(altura * altura)

    # calculando IMC
    print(f'Seu IMC é de: {calculo}\n')

    if calculo < 18.5:
        print(f'Magreza extrema!! {nome}, recomenda-se que procure engordar mais e consulte um medico.')
    if calculo > 18.5 and calculo < 24.9:
        print(f'{nome}, você está dentro dos padrões considerados normais.')
    if calculo > 25 and calculo < 29.9:
        print(f'{nome}, você está com sobre peso, pratique atividades fisicas leves acompanhado(a) de um profissional ebusque um especialista (nutricionista ou medico)')
    if calculo > 30 and calculo < 39.9:
        print(f'{nome}, você está com obesidade nivel 2, busque orientação medica!')
    else:
        print(f'{nome}, você está com obesidade GRAVE (nivel 3), busque orientação medica imediatamente!')


    #verifica se o usúario deseja continuar
    continuar = input('Deseja continuar (s/n)').lower()

    # Verifica a opção do usúario
    if continuar == 's':
        continue
    else:
        break