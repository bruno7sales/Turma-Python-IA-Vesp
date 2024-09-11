# Classe
class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
    
    # Metodos de acesso:
    @property
    def nome(self):
        return self.__nome
    
    # Metodo dset nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
        # Metodos de acesso:
    @property
    def idade(self):
        return self.__idade
    
    # Metodo dset nome
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
        
        # Metodos de acesso:
    @property
    def email(self):
        return self.__email
    
    # Metodo dset nome
    @email.setter
    def email(self, email):
        self.__email = email
        
    