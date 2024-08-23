
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    texto = input('Informe o texto a ser traduzido: ')
    texto_traduzido = tradutor.translate(texto)
    print( f'{texto_traduzido}\n')
    repetir = input('Deseja traduzir outro texto (s/n): ').lower()
    if repetir == 's':
        continue
    else:
        break
