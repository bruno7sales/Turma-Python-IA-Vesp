 # Superclasse, classe-pai, classe-base
class Pessoa:
     # Atributos
    def __init__(self, endereco, email, telefone):
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        
    # Metodo
    def mostrar_cartao_visita(self):
        print(f'Endereço {self.endereco }')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')
    
#subclasse, classe-filha, classe derivada de Pessoa Fisica
class PessoaFisica(Pessoa):
    # Polimorfismo do construtor
    def __init__(self, endereco, email, telefone, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        super().__init__(endereco, email, telefone)
    def mostrar_cartao_visita(self):
        print(f'Nome do usuário: {self.nome}.')
        print(f'CPF: {self.cpf}.')
        print(f'Profissão: {self.profissao}.')
        super().mostrar_cartao_visita()
        
class PessoaJuridica(Pessoa):
        def __init__(self, nome_fantasia, razao_social, cnpj, endereco, email, telefone):
            self.nome_fantasia = nome_fantasia
            self.razao_social = razao_social
            self.cnpj = cnpj
            super().__init__(endereco, email, telefone)
            
        def mostrar_cartao_visita(self):
            print(f'Nome da Empresa: {self.nome_fantasia}.')
            print(f'Razão Social: {self.razao_social}.')
            print(f'CNPJ: {self.cnpj}.')
            
            return super().mostrar_cartao_visita()