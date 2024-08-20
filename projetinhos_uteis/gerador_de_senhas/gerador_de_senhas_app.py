import secrets

while True:
    confirma = input('Gerar sneha(s/n)? ').lower()
    
    if confirma == 's':
        print(secrets.token_urlsafe(16))
        continue
    else:
        print('Progama encerrado!!')
        break