import os

categoria2 = './download/Categoria-1' # Ou outro endereço para onde você tenha extraído a pasta com os arquivos de poço
pocos = os.listdir(categoria2)

for pasta in pocos:
    query = os.listdir(f'{categoria2}/{pasta}/Perfil Convencional')
    for file in query:
        if file[-4:] == 'dlis':
            os.rename(f'{categoria2}/{pasta}/Perfil Convencional/{file}',f'./dados/{file}')