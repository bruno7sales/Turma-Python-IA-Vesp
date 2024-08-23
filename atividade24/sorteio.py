import random

nomes = []

while True:
    print('1 - Inserir na lista.')
    print('2 - Sortear.')
    print('0 - Sair do programa.')

    opcao = input('Opção desejada: ')
    match opcao:
       case '1':
         nome =  input('Insira o nome: ')
         nomes.append(nome)
         print(f'{nome} Inserido com secesso.') 
         continue

       case '2':
        nome_sorteado = random.randint(0, len(nomes)-1)
        print(f'nome soteado {nomes[nome_sorteado]}')
        continue
       
       case '0':
         print('Progama encerrado.')
         break
       
       case _:
          print('Opção invalida!')

