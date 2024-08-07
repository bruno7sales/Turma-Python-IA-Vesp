#Entrada de Dados
nome = input('Insira seu nome: ')
nota = str(input('Insira sua nota: ')).replace	(',', '.')

#Conversão (Aceitou Jesus \o/)
nota = float(nota)

#Verificação se o aluno passou ou não
if nota <= 10 and nota >= 0:
     if nota >= 7:
        print(f'{nome} está aprovado(a).')
     elif nota >= 5:
        print(f'{nome} está de recuperação.')
     else:
        print(f'{nome} está reprovado(a).')
else:
     print('Nota invalida!')

  