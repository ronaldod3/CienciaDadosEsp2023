"""
Módulo de Processamento
Descrição: Este módulo prevê o processamento de dados do Aplicativo de Interpolacao.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 05/12/2023

"""
# Importação das bibliotecas da geração de gráficos


from PIL import Image
from io import BytesIO

import requests
import json

def escritora(dados):
    if dados[1] == 'json':
        r = requests.get(dados[0], stream=True)
        page = r.json()
        with open('pagina.txt', 'w') as f:
            f.write(json.dumps(page))
    elif dados[1] == 'raw':
        r = requests.get('https://api.github.com/events')
        with open('pagina.txt', 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    else:
        i = Image.open(BytesIO(r.content))