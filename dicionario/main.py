# Dicionario
usuario = {
    'Nome': 'Alex Machado',
    'Idade': 39,
    'Profissão': 'progamador'
}

# Adicionar uma nova chave
'''usuario['email'] = 'alex@gmail.com'
'''

 # Exibindo valores do dicionario na tela
'''print('Nome:', usuario.get('nome'))
print('Idade:', usuario.get('idade'))
print('Profissão:', usuario.get('profissão'))
print('Email:', usuario.get('email'))'''


# Outra fora de exibir o Dicionario
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')

#Alterando o valor da chave
usuario['Nome'] = input('informe o novo nome: ')
usuario['Idade'] = input('informe a nova idade: ')
usuario['E-mail'] = input('informe o e-mail de usuário: ')


# Outra fora de exibir o Dicionario
print('\n')
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')


# Excluindo a chave
del usuario['Idade']
print('\n')
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')
