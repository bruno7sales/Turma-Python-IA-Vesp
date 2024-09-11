# NOTE: cria a classe

class Pessoa:
    
    # Os atributos são sempre definidos dentro do metodo construtor
    # NOTE: medo construtor
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        
    # NOTE: progama principal:
if __name__ == '__main__':
    nome = input('Informe o nome do usúario: ')
    idade = input('Informea idade do usúario: ')
    cpf = input('Informe o cpf do usúario: ')
    email = input('Informe o email do usúario: ')
    
    # Instancia do objeto
    ususario = Pessoa(nome, idade, cpf, email)
    
    # Saída de dados
    print(f'Nome: {ususario.nome}')
    print(f'Idade: {ususario.idade}')
    print(f'CPF: {ususario.cpf}')
    print(f'E-mail: {ususario.email}')