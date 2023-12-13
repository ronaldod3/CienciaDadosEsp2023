

def leitor_web():
    endereco_web = input('Informe o endereço da página (Ex: http://pythonscraping.com/pages/page1.html): ')
    #tag = input('Informe o que deseja extrair (Exemplo: title, head, body, etc.): ')
    tag = input('Informe a palavra chave que deseja procurar: ')
    return [endereco_web, tag]

def saida(soup, counter):
    print(f'O título da página é: \n{soup.title}')
    print(counter)
    
    
    
    #print(f'O {tag} da página é: \n{len(soup.find_all(tag))}')