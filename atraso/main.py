# Importando biblioteca
import time
import os

msgs = ('Abrindo porgama...', 'Exacutando progama...', 'Ainda executando o programa...', 'Progama demorando mais que o planejado...', 'Finalizando. Aguarde...', 'Progama executado e finalizado com sucesso.')

for msg in msgs:
    os.system('cls')
    print(msg)
    time.sleep(3)
