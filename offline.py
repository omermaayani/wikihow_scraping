from bs4 import BeautifulSoup

with open('wikiHow_ How-to instructions you can trust.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    links = soup.find_all('a', class_ =  'hp_thumb_a')
    for link in links:
        link_name = link.p.text
        link_addr = link['href']
        print(link_name)
        print(link_addr)