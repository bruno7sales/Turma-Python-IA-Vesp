# Importando biblioteca
import calendar
from datetime import date

# Ecibindo a data atual
dia = date.today().day
mes = date.today().month
ano = date.today().year

# Tupla dos meses do ano
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Saida de dados
print('\n')
print(f'Data atual: {dia}/{meses[mes - 1]}/{ano}.')
print('\n')
print(calendar.month(ano, mes))
