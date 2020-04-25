import requests
from bs4 import BeautifulSoup

def parse(search):
    #search=input("Введите понятие:   ")
    URL=f"https://ru.wikipedia.org/wiki/{search}"
    HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    response=requests.get(URL, headers=HEADERS)
    soup=BeautifulSoup(response.content,'html.parser')
    items=soup.body('p',limit=1)
    return items




parse('Суп')
