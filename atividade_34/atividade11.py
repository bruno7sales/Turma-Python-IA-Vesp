import os

quadrado = lambda l: 1**2
circulo = lambda r: 3.14*r**2
triangulo = lambda b,h: (b*h)/2
trapezio = lambda b_maior, b_menor, h: ((b_maior+b_menor)*h)/2
if __name__ == "__main__":
    while True:
        print('1 - Quadrado.')
        print('2 - circulo.')
        print('3 - Triângulo.')
        print('4 - Trapézio.')
        print('0 - Sair.')

        opcao = input('Opção desejada: ')

        os.system('cls')

        match opcao:
            case '1':
                
