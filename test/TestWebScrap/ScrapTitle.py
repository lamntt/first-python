import requests
import bs4
result = requests.get('http://www.example.com')
print(result.text)


soup = bs4.BeautifulSoup(result.text,'lxml')
# print(soup)
tag = soup.select('p')
print(tag[1].getText())
