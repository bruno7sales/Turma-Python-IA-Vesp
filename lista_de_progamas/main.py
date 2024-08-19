import winapps

for item in winapps.list_installed():
    print(f'Progama: {item.name}.')
    print(f'Versão: {item.version}.')
    print(f'Data de instalção: {item.install_date}.')
    print(f'Data de publicação: {item.publisher}.')
    print(f'local da desinstalção:  {item.uninstall_string}.')
    print('-' * 50)