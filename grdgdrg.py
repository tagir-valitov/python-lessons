import requests
from requests import Session
from bs4 import BeautifulSoup
#API_CASE = 'baf810b8d72076e247aab1a890a25a3f'
#data = {"custname": "Тагир Шамилевич Валитов",
        #"custtel": "+79179077347",
        #"custemail": "tagirvalitov614@gmail.com",
        #"size": "medium",
        #"topping": "onion",
        #"delivery": "",
        #"comments": "",}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36"}
base_url = "https://scrapingclub.com/exercise/list_infinite_scroll/"


def main(base_url):
    s = Session()
    s.headers.update(headers)#добовляем в словарь headers

    response = s.get(base_url)
    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all('div', class_="col-lg-4 col-md-6 md-4")




#response = requests.get(url).json()
#print(response['title'])
#print(response['price'])
#print(response['description'])
main(base_url)