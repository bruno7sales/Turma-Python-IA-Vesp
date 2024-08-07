# Lista
cidades = ['Brasilia', 'Taguatinga', 'Planaltina', 'Ceilandia', 'Samambaia', 'Riacho fundo', 'Candogolandia', 'Nucleo bandeirante', 'Gama', 'Santa MAria', 'Sobradinho', 'Planaltina', 'Recanto das Emas', 'Guará', 'Valparaiso', 'Novo gama', 'Ceu azul', 'Lago azul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueira', 'Areal', 'Sol nascente', 'Dvo', 'São sebastião', 'Dvo']

# Usuário pesquisa pela cidade
cidade_pesquisada = input('Cidade a ser pesquisada: ')

# Verifica se a cidade exisite
try:
    # Pega o indice do item da pesquisa
    indice = cidades.index(cidade_pesquisada)
    print(f'{cidade_pesquisada} encontrada no indice {indice}.')
except:
    print(f'Não foi possivel encontra a cidade: {cidade_pesquisada}')
