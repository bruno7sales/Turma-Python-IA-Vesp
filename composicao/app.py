if __name__ == "__main__":
    # Instancia dos objetos
    endereco_pessoal = Endereco('', '', '', '')
    telefone_usuario = Telefone('')
    usuario = Pessoa('', 0,'','')
    

    # Entrada de dados
    usuario.nome = input('Informe o nome do usuario: ')
    usuario.idade = int(input('Informe a idade do usuario: '))

    
    # composicao usuario-endereco
    usuario.endereco = endereco_pessoal
    usuario.telefone = telefone_usuario

    # entrada de dado do endereco
    usuario.endereco.cep = input("Informe o CEP: ")
    usuario.endereco.uf = input("Informe o UF: ")
    usuario.endereco.cidade = input("Informe a cidade: ")
    usuario.endereco.bairro = input("Informe o bairro: ")
    usuario.telefone.tel_pessoal = input("Informe o numero pessoal: ")
    

    
    # Saída de dados 
    print(usuario.obter_info_pessoal())
    
