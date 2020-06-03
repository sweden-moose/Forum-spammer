from bs4 import BeautifulSoup
import requests as req


def find_pages(link):
    pages = 1
    resp = req.get(link)
    find_soup = BeautifulSoup(resp.text, 'lxml')
    n = find_soup.select('li a')
    for i in n:
        try:
            if i['title'].startswith('Перейти к странице'):
                tmp = i['title'].split()
                all.append(tmp[-1])
                if int(tmp[-1]) > pages:
                    pages = int(tmp[-1])
        except BaseException:
            pass
    return pages


def find_threads(link):
    ans = []
    for j in range(1,find_pages(link)):
        resp = req.get(f'{link}/page-{j}')
        soup = BeautifulSoup(resp.text, 'lxml')
        b = [item['href'] for item in soup.select('h3 a')]
        for i in b:
            if i.startswith('http'):
                ans.append(i)
    return ans

# print(find_pages('https://freetp.org/forum/categories-10'))
# print(find_threads('https://freetp.org/forum/categories-10'))