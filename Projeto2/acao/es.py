from proc import Acao

def leitora_emissor() -> str:
    '''Esta funcao recebe o emissor da Ação'''
    emissor = input('Qual o nome da empresa? ')
    return emissor

def leitora_codigo() -> str:
    '''Esta funcao recebe o código da Ação'''
    codigo = input('Qual o código na B3? ')
    return codigo

def leitora():
    '''Esta funcao le o emissor e código da Ação'''
    emissor = leitora_emissor()
    codigo = leitora_codigo()
    return [emissor, codigo]

def impressora(acao: Acao):
    '''Esta funcao imprime o resultado'''
    print(acao)