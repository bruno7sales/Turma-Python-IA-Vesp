
#criando uma classe
class Carro:
    # atributos
    fabricante = 'Volkswagen'
    modelo = 'Gol'
    ano = '2000'
    cor = 'Preto'
    placa = 'ABC-1234'
    
    #metodos
    def ligar(self, ignicao):
        if ignicao:
            return f'{self.modelo} está ligado'
        else:
            return f'{self.modelo} está desligado'
        
# NOTE: programa principal
if __name__ == '__main__':
    # intancia a classe carro (criar objeto)
    meu_carro = Carro()
    
    # Exibir os atributos do objeto
    print(f'Fabricante: {meu_carro.fabricante}.')
    print(f'Fabricante: {meu_carro.modelo}.')
    print(f'Fabricante: {meu_carro.ano}.')
    print(f'Fabricante: {meu_carro.cor}.')
    print(f'Fabricante: {meu_carro.placa}.')

    ignicao = True

    print(meu_carro.ligar(ignicao))

