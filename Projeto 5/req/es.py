"""
Módulo Entrada e Saída
Descrição: Este módulo prevê funções de entrada e saída de dados para Aplicativo de Plotagem.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 04/12/2023

"""

def leitora():
    pagina = input("Digite a página que deseja ler no formato https://pagina.da.web? ")
    formato = input("Digite o formato que deseja ler os dados webpage ('json', 'raw', 'imagem')? ")
    return [pagina, formato]

def impressora_web(dados, r):
    if dados[1] == 'raw':
        for chunk in r.iter_content(chunk_size=128):
            print(chunk)
    elif dados[1] == 'json':
        page = r.json()
        print(page)
    
    print('\n A página da web contém as informações acima e foram salvas no arquivo pagina.txt.')
    
    
    