from dataclasses import dataclass

@dataclass
class Pessoa: 
    # atributos
    nome: str
    idade: int
    altura: float
    
    def __str__(self):
        return f"Ola meu nome e {self.nome} tenho {self.idade} anos e {self.altura} metros de altura."
    
    def __del__(self):
        return f"{self.nome} destruido com sucesso."
        