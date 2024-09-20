import requests
from bs4 import BeautifulSoup

news_res=requests.get('https://www.bbc.com/news')
soup=BeautifulSoup(news_res.content,'html.parser')
headings=soup.find_all('h2')
with open('news_headings.text','w',encoding='UTF-8') as news_file:
    for heading in headings:
        news_file.write(heading.text +'\n')

print('bbc news printed')        
