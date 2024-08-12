# Dicionario
usuario = {}

# Inserindo valores
usuario['Nome'] = input('informe o nome: ')
usuario['CPF'] = input('informe o CPF: ')
usuario['RG'] = input('informe o RG: ')
usuario['Data de Nascimento'] = input('informe a data de nascimento: ')
usuario['Sexo'] = input('informe o sexo (masculino e feminino): ')
usuario['Signo'] = input('informe o signo: ')
usuario['Nome da mãe'] = input('informe o nome da mãe: ')
usuario['Nome do pai'] = input('informe o nome do pai: ')
usuario['E-mail'] = input('informe o e-mail: ')
usuario['Senha'] = input('informe a senha: ')
usuario['CEP'] = input('informe o CEP: ')
usuario['Endereço'] = input('informe o endereço: ')
usuario['Bairro'] = input('informe o bairro: ')
usuario['Número'] = input('informe o número: ')
usuario['Cidade'] = input('informe a cidade: ')
usuario['Estado'] = input('informe o estado: ')
usuario['Telefone'] = input('informe o número de telefone: ')
usuario['Telefone Celular'] = input('informe o número de telefone celular: ')
usuario['Altura'] = input('informe a altura: ')
usuario['Peso'] = input('informe o peso: ')
usuario['Tipo Sanguineo'] = input('informe o tipo sanguineo: ')
usuario['Cor favorita'] = input('informe sua cor favorita: ')

# Quebra de linha
print('\n')

# imprimindo dados
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')

