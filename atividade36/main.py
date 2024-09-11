import random 

class Pessoa:
    def __init__(self, nome, humor):
        self.nome = nome
        self.humor = humor
        
    def cumprimentar (self):
        if self.humor:
            print(f'Olá, meu nome é {self.nome}. Qual é seu nome?')
        else:
            print(f'Tá olhando o que?? Mané')
    def responder (self, nome, humor):
        if humor:
            print(f'Olá {nome}, meu nome é {self.nome}. Prazer em te conhecer!!')
        else:
            print('Vai se lascar')
            self.humor = False
        return self.humor
    
if __name__ == '__main__':
    humores = (True, False)
    nome1 = input('Informe o nome de 1° usúario: ')
    nome2 = input('Informe o nomee do segundo usúario: ')
    
    usuario1 = Pessoa(nome1, humores[random.randint(0,1)])
    usuario2 = Pessoa(nome2, humores[random.randint(0,1)])
    
    usuario1.cumprimentar()
    usuario1.humor = usuario2.responder(usuario1.nome, usuario2.humor)
    
    if usuario1.humor:
        print(f'{usuario1.nome} ficou feliz .')
    else:
        print(f'{usuario1.nome} ficou triste.')
        
        