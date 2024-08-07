#Entrada de Dados
nome = input('Informe seu nome: ')

#Lista de Cursos:
print(F'{'='*30} LISTA DE CURSOS {'='*30}\n')
print('1 - Operador de Micro.')
print('2 - Desenvolvedor Java.')
print('3 - Desenvolvedor Python.')
print('4- Desenvolvedor Front-End.')
print('5- Montador e reparador de Micro.')

opcao = input('\n Escolha sua opção de curso: ')

# O "switch..case" do python
match int(opcao):
    case 1:
        print(f'{nome} matriculo-se no curso de Operador de Micro.')
    case 2:
         print(f'{nome} matriculo-se no curso de Java.')
    case 3:
         print(f'{nome} matriculo-se no curso de Python.')
    case 4:
         print(f'{nome} matriculo-se no curso de Front-End.')
    case 5:
         print(f'{nome} matriculo-se no curso de reparador de Micro')
    #Default
    case _:
          print('Opção invalida!')

