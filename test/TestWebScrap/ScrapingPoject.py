import requests
import bs4

base_url = 'http://quotes.toscrape.com/page/{}/'
res = requests.get(base_url.format('1'))
sp = bs4.BeautifulSoup(res.text,'lxml')
ex = sp.select('.author')
authors = []
# for author in ex:
#     authors.append(author.text)
# # print(authors)

ex2 = sp.select('.text')
quosts = set()
for quost in ex2:
    quosts.add(quost.text)
# print(quosts)

ex3 = sp.select('.tag-item')
tags = []
for tag in ex3:
    tags.append(tag.text.rstrip('\n').lstrip('\n'))
# print(tags)

for page in range(1,50):
    url = base_url.format(page)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    auth = soup.select('.author')
    for author in auth:
        authors.append(author.text)
print(set(authors))
