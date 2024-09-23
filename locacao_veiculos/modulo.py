class Cliente:
    def __init__(self, nome, documento, idade):
        self.nome = nome
        self.documento = documento
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Documento: {self.documento}, Idade: {self.idade}"


class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria

    def __str__(self):
        return f"Modelo: {self.modelo}, Placa: {self.placa}, Valor Diária: R${self.valor_diaria:.2f}"


class SistemaLocacao:
    def __init__(self):
        self.veiculos_disponiveis = [
            Veiculo("Fusca", "ABC-1234", 100.0),
            Veiculo("Civic", "XYZ-5678", 150.0),
            Veiculo("Forte", "LMN-9876", 200.0),
            Veiculo("Corolla", "JKL-5432", 180.0),
            Veiculo("Palio", "DEF-1111", 90.0)
        ]

    def cadastrar_cliente(self):
        nome = input("Digite seu nome: ")
        documento = input("Digite seu documento: ")
        idade = int(input("Digite sua idade: "))
        return Cliente(nome, documento, idade)

    def exibir_veiculos(self):
        print("\nVeículos disponíveis:")
        for i, veiculo in enumerate(self.veiculos_disponiveis, start=1):
            print(f"{i}. {veiculo}")

    def escolher_veiculo(self):
        while True:
            try:
                escolha = int(input("Escolha o número do veículo que deseja alugar: "))
                if 1 <= escolha <= len(self.veiculos_disponiveis):
                    return self.veiculos_disponiveis[escolha - 1]
                else:
                    print("Escolha um número válido.")
            except ValueError:
                print("Por favor, insira um número válido.")

    def locar_veiculo(self):
        cliente = self.cadastrar_cliente()
        
        if cliente.idade < 18:
            print("Desculpe, você deve ter pelo menos 18 anos para alugar um veículo.")
            return
        
        self.exibir_veiculos()
        veiculo_escolhido = self.escolher_veiculo()

        print("\nLocação realizada com sucesso!")
        print("Dados do Cliente:")
        print(cliente)
        print("Dados do Veículo Alugado:")
        print(veiculo_escolhido)


if __name__ == "__main__":
    sistema = SistemaLocacao()
    sistema.locar_veiculo()

