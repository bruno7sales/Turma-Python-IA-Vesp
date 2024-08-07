# Lista
cidades = ['Brasilia', 'Taguatinga', 'Planaltina', 'Ceilandia', 'Samambaia', 'Riacho fundo', 'Candogolandia', 'Nucleo bandeirante', 'Gama', 'Santa MAria', 'Sobradinho', 'Planaltina', 'Recanto das Emas', 'Guará', 'Valparaiso', 'Novo gama', 'Ceu azul', 'Lago azul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueira', 'Areal', 'Sol nascente', 'Dvo', 'São sebastião', 'Dvo']

# Usuário informa o valor a ser pesquisado
cidade_pesquisa = input('Cidade a ser pesquisada: ').capitalize()

#Verificação se a cidade existe
if cidade_pesquisa in cidades:
    print(f'Cidade: {cidade_pesquisa} encotrada com suceeso')
else:
    print('Não foi possivel encontrar a cidade!')

