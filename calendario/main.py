'''
# importa biblioteca
import calendar
from datetime import date

# Exibe o calneadrio do ano atual
for mes in range(1, 13):
    print(calendar.month(date.today(). year, mes)) #<--- imprime o ano automaticamente puxando da biblioteca!!!
    '''

# importa biblioteca
import calendar
from datetime import date

try: 
    print('\n')
    ano = int(input('Informe o ano: '))
    print('\n')
# Exibe o calneadrio do ano atual
    for mes in range(1, 13):
     print(calendar.month(ano, mes))
except:
   print('Não foi possivel exibir o calendário!')
