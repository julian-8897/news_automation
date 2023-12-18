from bs4 import BeautifulSoup
import requests

class WebScraper:
    def scrape(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return ' '.join(map(lambda p: p.text, soup.find_all('p')))