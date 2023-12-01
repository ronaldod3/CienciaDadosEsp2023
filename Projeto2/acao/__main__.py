# Importação dos módulos
import es
from proc import Acao

#Definicao de funções

def main():
    # Leitura de Dados
    dados = es.leitora()
    
    # Instanciamento do objeto
    acao = Acao(dados[0], dados[1])
    
    #Saida de dados
    es.impressora(acao)
    
# Execução

if __name__ == '__main__':
    main()