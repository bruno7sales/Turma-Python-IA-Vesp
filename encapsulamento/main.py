# Entrada de Dados:

import classe as cl

if __name__ == '__main__':
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    email = input('Informe o e-mail: ')
    
    # Instancia de classe:
    usuario = cl.Pessoa(nome, idade, email)
    
    # Saída de Dados
    print(f'Nome: {usuario.__nome}.')
    print(f'Idade: {usuario.__idade}.')
    print(f'E-mail: {usuario.__email}.') 