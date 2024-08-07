# Lista
cidades = ['Brasilia', 'Taguatinga', 'Planaltina', 'Ceilandia', 'Samambaia', 'Riacho fundo', 'Candogolandia', 'Nucleo bandeirante', 'Gama', 'Santa MAria', 'Sobradinho', 'Planaltina', 'Recanto das Emas', 'Guará', 'Valparaiso', 'Novo gama', 'Ceu azul', 'Lago azul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueira', 'Areal', 'Sol nascente', 'Dvo', 'São sebastião', 'Dvo']

# Cidade a ser pesquisaa
cidade_pesquisada = input("Cidade a ser pesquisada: ").capitalize()

# Contar quantidade de ocorrencias de palavras
cont = cidades.count(cidade_pesquisada)

# Exibe o resultado
print(f'{cidade_pesquisada} foi encontrada {cont} vezes')
