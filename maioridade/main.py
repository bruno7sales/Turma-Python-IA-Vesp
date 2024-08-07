# Executando Loop Infinito
while True:
    # Entrada de Dados
    nome = input('Informe seu nome: ')
    idade = int(input ('Informe sua idade: '))

    #Verificando a maioridade do úsuario
    if idade >= 18:
        print(f'{nome} é maior de idade.')
    else:
        print(f'{nome} é menor de idade.')

    #verifica se p usúario deseja continuar
    continuar = input('Deseja continuar (s/n)').lower()

    # Verifica a opção do usúario
    if continuar == 's':
        continue
    else:
        break


