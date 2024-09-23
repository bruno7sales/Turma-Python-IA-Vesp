from modulo import *

if __name__ == "__main__":
    usuario = Pessoa('',0,'')

    usuario.nome = input("Informe o nome: ")
    usuario.idade = int(input("Informe o idade: "))
    usuario.email = input("Informe o email: ")
 
    print(usuario.nome) 
    print(usuario.idade) 
    print(usuario.email) 
     

    print(str(usuario))
    print(repr(usuario))
    
    