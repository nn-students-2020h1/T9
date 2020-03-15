import requests
from bs4 import BeautifulSoup


def getCatImage():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    imgData = response.json()
    return imgData[0]["url"]


def getQuote():
    html = requests.get("https://icitaty.ru/random/").text
    soup = BeautifulSoup(html, "lxml")

    text = soup.find("p").text
    author = soup.find("a", attrs={"title": "Автор цитаты"})
    book = soup.find("a", attrs={"title": "Цитаты из книги"})
    person = soup.find("a", attrs={"title": "Цитируемый персонаж"})

    author = str(author)[str(author).find("</i>") + 4:str(author).find("</a>")]
    book = str(book)[str(book).find("</i>") + 4:str(book).find("</a>")]
    person = str(person)[str(person).find("</i>") + 4:str(person).find("</a>")]

    author = ' '.join(author.split())
    book = ' '.join(book.split())
    person = ' '.join(person.split())

    return text, author, book, person


def getCatFact():
    response = requests.get('https://cat-fact.herokuapp.com/facts/random')
    data = response.json()
    return data['text']
