"""
Módulo Proc
Descrição: Este módulo provê as funções da classe.
Autor: Ronaldo Debiasi
Versão: 0.0.1
Data: 30/11/2023

"""

class Acao:
    def __init__(self, emissor, codigo_b3):
        self.emissor = emissor
        self.codigo_b3 = codigo_b3
    def __str__(self):
        return (f'Este é o objeto da classe Ação e o emissor da ação é {self.emissor} e o código é {self.codigo_b3}')
    def negociar(self):
        return ('Metodo negociar() nao implementado')