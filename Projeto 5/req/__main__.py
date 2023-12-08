"""
Módulo Principal

#ALTERAR
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

# Importação dos módulos


import es
import proc

import requests
import json

from PIL import Image
from io import BytesIO


def main():
    dados = es.leitora()
    
    proc.escritora(dados)

    if dados[1] != 'imagem':
        es.impressora_web(dados, r)
      
if __name__ == "__main__":
    main()
    