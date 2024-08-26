import os

# Exibe menu
def exibe_menu():
    print('\n') 
    print('1 - Ler arquivo.')
    print('2 - Gravar novos dados no arquivo.')
    print('0 - Encerrar progama.')

# Funçãp para gravar novos dados
def gravar_arquivos(dados, nome, email, profissao):
    dados += f'\n\n{'-'*30}\n\nNome:{nome}\nEmail:{email}\nProfissão:{profissao}'
    with open('arquivo.txt', 'w', encoding = 'utf-8') as arquivo:
        arquivo.write(dados)

# Funçãp de leitura de arquivo
def ler_arquivo():
    with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()
    return dados

# Progama principal
if __name__ == '__main__':
    while True: 
        dados = ler_arquivo() 
        print(ler_arquivo())
        exibe_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')
        match opcao:
            case '1':
                print(f'\n{dados}\n')
                continue
            case'2':
                print('NOVO CADASTRO \n')
                novo_nome = input('Informe o nome do novo usúario: ')
                novo_email = input('informe o email do nvo usúario: ')
                nova_profissão = input('Informe a profissãp do novo usúario: ')
                gravar_arquivos(dados, novo_nome,novo_email,nova_profissão)
                continue
            case'0':
                print('Progama encerrado com sucesso!!')
                break
            case _:
                print('Opção inválida.')
                continue



