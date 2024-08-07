#Importando bibliotecas:
import os
import time

# Entrada de dados
numero = int(input('informe um número inteiro: '))


while numero >= 0:
    os.system('cls')
    print('\n Contagem Regressiva: ')
    print(f'{numero}...')
    numero -= 1
    time.sleep(0.2)

print('KBUMMMMMMMMMMMM!!!!!!!!!!!!!')
    
