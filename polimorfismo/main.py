import classes as cl

if __name__ == '__main__':
    # Entrada de dados:
    nome = input('Informe o nome do usuário: ')
    email = input('Informe o e-mail do usuário: ')
    cpf = input('Informe o CPF do usuário: ')
    profissao = input('Informe a profissão do usuário: ')
    endereco = input('Informe o endereço do usuário: ')
    telefone = input('Informe o tlefone do usuário: ')
    
    # Instanciar a pessoa física:
    usuario = cl.PessoaFisica(endereco, email, telefone, nome, cpf, profissao)
    
    # Entradad de dados
    nome_fantasia = input('Informe o Nome Fantasia da Empresa: ')
    email = input('Informe o e-mail da Empresa: ')
    cnpj = input('Informe o CNPJ da Empresa: ')
    razao_social = input('informe o a razao social: ')
    endereco = input('Informe o endereço da Empresa: ')
    telefone = input('Informe o telefone da Empresa: ')
    
    # Instancia a classe Pessoa Juridica:
    empresa = cl.PessoaJuridica(nome_fantasia, razao_social, cnpj, endereco, email, telefone)
    usuario.mostrar_cartao_visita()
    print('-' *10)
    empresa.mostrar_cartao_visita()
    