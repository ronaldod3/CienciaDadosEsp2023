def leitora_operacao() -> str:
    """Esta funcao le a operação a ser realizada."""
    operacao = input("""Digite a operação que deseja realizar. 
Pressione + para adição; 
- para subtração; 
* para multiplicação; 
/ para divisão""")
    return operacao

def leitora_numeros() -> list:
    """Esta funcao le dois numeros e os coloca em uma lista."""
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f'Digite o número {i+1} que deseja operar:')))
        i += 1
    return numeros

def leitora() -> list:
    """Esta funcao le os dados das funcoes leitora_numeros e leitora_operacao e salva em uma lista."""
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]

def escritora(resultado: float) -> None:
    '''Esta funcao apresenta o resultado na tela.'''
    print(f'O resultado da operação é igual a {resultado}.')