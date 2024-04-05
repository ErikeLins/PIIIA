import requests
from bs4 import BeautifulSoup


# URL da página que foi feito a raspagem
url = "https://nahoradoocio.lowlevel.com.br/2020/06/08/8-series-sobre-a-luta-contra-o-racismo/"

status_ok = 200

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
}
# Fazendo uma solicitação GET para obter o conteúdo da página
response = requests.get(url, headers=headers)


# Verificar se a solicitação foi bem sucedida (status code 200)
if response.status_code == status_ok:
    html = response.text
    # Passando o conteúdo HTML para o BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Encontrando todos os elementos <h2> que contêm <strong>
    posts = soup.find_all(lambda tag: tag.name == 'h2' and tag.find('strong'))
    
    # Encontrando todos os elementos <h2> que contêm <strong>
    posts = soup.find_all(lambda tag: tag.name == 'h2' and tag.find('strong'))
    
    # Iterando sobre os posts para extrair os nomes e descrições dos filmes
    for post in posts:
        # Nome do filme
        movie_name = post.text.strip()
        
        # Descrição do filme (procurando o próximo elemento irmão)
        description = post.find_next_sibling('p').text.strip()
        
        # Imprimir nome e descrição do filme
        print("Nome do filme:", movie_name)
        print("Descrição:", description)
        print()
else:
    print("Falha ao carregar a página. Status code:", response.status_code)
