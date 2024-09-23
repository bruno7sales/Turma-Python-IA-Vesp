from modulo import *

if __name__ == "__main__":
    usuario = Pessoa('', 0, 0.00)
    
    usuario.nome = input("Informe o nome: ")
    usuario.idade = int(input("Informe a idade: "))
    usuario.altura = float(input("Informe a altura: ").replace(',','.'))

    print(str(usuario))   