from modulo import *

if __name__ == "__main__":
    aluno1 = Aluno('', '', '')

aluno1.nome = input('Informe o nome do aluno: ')
aluno1.matricula = input('Informe o numero de matricula do aluno: ')
aluno1.cpf = input('Informe o CPF do aluno: ')

aluno2 = Aluno('', '', '')

aluno2.nome = input('\nInforme o nome do 2° aluno: ')
aluno2.matricula = input('Informe o numero de matricula do 2° aluno: ')
aluno2.cpf = input('Informe o CPF do 2° aluno: ')


curso1 = Curso('', 0, '')

curso1.nome = input('\nInforme o nome do curso: ')
curso1.duracao = input('Informe a duração do curso: ')
curso1.turno = input('Informe o turno do curso: ')

# Curso 2
curso2 = Curso('', 0, '')

curso1.nome = input('\nInforme o nome do 2° curso: ')
curso1.duracao = input('Informe a duração do 2° curso: ')
curso1.turno = input('Informe o turno do 2° curso: ')

# Cadastrando os alunos intanciados no curso instaciado
aluno1.inscrever_curso(curso1)
aluno1.inscrever_curso(curso2)
aluno2.inscrever_curso(curso1)

# Saida de dados
print(f'Aluno {aluno1.nome} de matricula  {aluno1.matricula} está inscrito no curso {aluno1.listar_curso()}.')
print(f'Aluno {aluno2.nome} de matricula  {aluno2.matricula} está inscrito no curso {aluno2.listar_curso()}.')
print(f'No curso {curso1.nome} estao matriculados os alunos: {curso1.listar_alunos()}.')
print(f'No curso {curso2.nome} estao matriculados os alunos: {curso2.listar_alunos()}.')


