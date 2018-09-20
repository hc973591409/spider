from bs4 import BeautifulSoup


soup = BeautifulSoup(open('../meinv.html'), 'lxml')

print(soup.select('a[class="search_btn"]'))