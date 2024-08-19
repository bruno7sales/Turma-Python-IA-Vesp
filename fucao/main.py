# Função de boas vindas
def saudar(nome, idade):
    if idade >= 18:
        print(f'{nome}, seja bem vindo(a) ao curso de Python!')
    else:
       print(f'{nome}, você teve a inscrição bloqueada.')
# Progama Principal
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))

# Executando a função
saudar(nome, idade)

