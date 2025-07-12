# Class for scrap offers in "Portisur"
import requests
from bs4 import BeautifulSoup

class Portisur():
    url = 'https://www.portisur.com.uy/'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com/',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    def obtener_ofertas(self):
        ofertas = self.soup.find_all('div', id='ofertasHome')
        MSG = ''
        for oferta in ofertas:
            titulo = oferta.find('div', class_='title-sale-of-day')
            items = oferta.find_all('div', class_='item-box')
            print(titulo.text)
            MSG += titulo.text + '\n'
            for item in items:
                description = item.find('div', class_='short-description')
                description_text = description.text if description else ''
                nombre = item.find('h2', class_='title').text + ' ' + description_text
                precio = item.find('span', class_='actual-price').text
                MSG += "- " + nombre + ' ' + precio + '\n'
                print("- ", nombre, precio)
        return MSG
        

p = Portisur()
ofertas = p.obtener_ofertas()


    