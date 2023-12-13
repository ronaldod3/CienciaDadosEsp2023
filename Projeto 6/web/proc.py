
import requests
from bs4 import BeautifulSoup

def leitor_web(endereco_web: str) -> str:
    pagina = requests.get(endereco_web)
    return pagina.text

def extrator(pagina_web: str) -> str:
    soup = BeautifulSoup(pagina_web, 'html.parser')   
    return soup

def counter(pagina_web, word):
    soup = BeautifulSoup(pagina_web, 'html.parser')   
    words = str(soup.find(text=lambda text: text and word in text))
    return words