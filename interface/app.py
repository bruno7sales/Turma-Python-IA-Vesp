from modolo import *

if __name__ == "__main__":
    
    cc = ContaCorrente('', '', '1001-1', '10010-1', 0)
    
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o CPF do titular: ')

    print(f'Nome: {cc.nome}.')
    print(f'CPF: {cc.cpf}.')
    print(f'Agência: {cc.agencia}.')
    print(f'Conta: {cc.conta}.')

    ...
    
