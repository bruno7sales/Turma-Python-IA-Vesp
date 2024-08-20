def mostra_menu():
    print('1 - Calcular energia potêncial.')
    print('2 - Calcular energia cinética.')
    print('0 - Sair do progama.')

def calcular_ep(m , h):
    ep = m*9.8*h
    return ep
def calcular_ec(m, v):
    ec = (m*(v*v))/2
    return ec


    