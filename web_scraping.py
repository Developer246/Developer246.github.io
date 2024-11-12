import requests
from bs4 import BeautifulSoup

def bing_search(query):
    # Realiza una búsqueda en Bing
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(f"https://www.bing.com/search?q={query}", headers=headers)
    
    # Analiza el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra todos los resultados de búsqueda
    results = soup.find_all('li', {'class': 'b_algo'})
    
    # Extrae y muestra los títulos y enlaces de los resultados
    for result in results:
        title = result.find('a').text
        link = result.find('a')['href']
        snippet = result.find('p').text if result.find('p') else "No description"
        print(f'Title: {title}\nLink: {link}\nSnippet: {snippet}\n')

# Uso de la función
query = "Python web scraping"
bing_search(query)
