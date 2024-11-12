from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def bing_search(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(f"https://www.bing.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('li', {'class': 'b_algo'})
    output = []
    for result in results:
        title = result.find('a').text
        link = result.find('a')['href']
        snippet = result.find('p').text if result.find('p') else "No description"
        output.append({'title': title, 'link': link, 'snippet': snippet})
    return output

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')
    results = bing_search(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
