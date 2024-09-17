from modulo import *

if __name__ == "__main__":
 
 # Instanciar objeto da subclasse
 h = Filho('', '', '', '', 0.0, 0.0, '')

 # Entrada de Dados
 h.nome = input('Informe o nome do herdeiro: ')
 h.email = input('Informe o e-mail do herdeiro: ')
 h.profissao = input('Informe o profissão do herdeiro: ')
 h.olhos = input('Informe a cor dos olhos do herdeiro: ')
 h.peso = float(input('Informe o peso do herdeiro: ').replace(',', '.'))
 h.altura = float(input('Informe a altura do herdeiro: ').replace(',', '.'))
 h.cor_cabelo = input('Informe a cor do cabelo do herdeiro: ')

h.exibir_cartao_de_visitas()
h.exibir_fisico()