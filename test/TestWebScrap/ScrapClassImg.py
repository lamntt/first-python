import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(result.text,'lxml')
for item in soup.select('.toctext'):
    print(item.text)


res= requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
sp = bs4.BeautifulSoup(res.text,'lxml')
item = sp.select('.image img')
print(len(item))
computer = item[0]
print(computer['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
f = open('image_scraping.jpg','wb')
f.write(image_link.content)
f.close()