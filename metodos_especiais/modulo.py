class Pessoa:
    # Metodo construtor
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

# MEtodos especiais

# NOTE a função str serve para retornar representação de valores que sejam legiveis para as pessoas.

def __str__(self):
    return f"Olá meu nome é {self.__nome}, tenho {self.__idade} e meu e-mail é {self.__email}."

# NOTE é função repr() ´w para gerar representações que o intepretador Pytoh consegue ter (ou levantará uma exceção SyntaxError, se não houver sintaxe equivalente).
def __repr__(self):
    return f"Pessoa {self.__nome}, {self.__idade}, {self.__email}."

def __len__(self):
    return self.__nome

def __del__(self):
    print(f'O objeto {self.__nome} foi eliminado com sucesso.')

    
