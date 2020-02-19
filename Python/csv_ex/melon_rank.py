import requests, csv
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'

headers = {
    'User-Agent': user_agent
}
res = requests.get(url, headers=headers).text

html = BeautifulSoup(res, 'html.parser')
rank = html.select('#lst50 > td:nth-child(2) > div > span.rank') # select는 이것좀 찾아줘~~
title = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
singer = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span')

melon_top_50 = []
for i in range(50):
    melon_top_50_dict = {
        'rank': f'{rank[i].text}위',
        'title': title[i].text,
        'singer': singer[i].text,
    }

    melon_top_50.append(melon_top_50_dict)

with open('melon_ranking.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['rank', 'title', 'singer']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for melon in melon_top_50:
        csv_writer.writerow(melon)