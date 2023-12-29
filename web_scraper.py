from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# class WebScraper:
#     def scrape(self, url):
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         return ' '.join(map(lambda p: p.text, soup.find_all('p')))
    

class WebScraper:
    def scrape(self, url):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Set path to chromedriver as per your configuration
        webdriver_service = Service(ChromeDriverManager().install())

        # Choose Chrome Browser
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        driver.get(url)

        # Wait for the dynamic content to load
        driver.implicitly_wait(10)

        paragraphs = driver.find_elements(By.TAG_NAME, 'p')
        text = ' '.join([p.text for p in paragraphs])

        driver.quit()

        return text