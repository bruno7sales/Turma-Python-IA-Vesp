#Importando bibliotecas:
import os
import time

# Entrada de dados
numero = int(input('informe um número inteiro: '))


while numero >= 0:
    os.system('cls')
    print('\nContagem Regressiva: ')
    print(f'{numero}...')
    numero -= 1
    time.sleep(0.7)

print('SEU TEMPO ACABOU!!!')