from bs4 import BeautifulSoup
import codecs

f= codecs.open("page_source.html", 'r', 'utf-8')
html = f.read()

soup = BeautifulSoup(html, "lxml")

data = []
table = soup.find_all('table')[1]
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
for i in range(len(data)):
    print(data[i])

    
