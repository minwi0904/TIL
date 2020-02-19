import requests, csv

from bs4 import BeautifulSoup

url = 'https://www.daum.net'

res = requests.get(url).text
html = BeautifulSoup(res, 'html.parser')
data = html.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div > ol > li > div > div:nth-child(1) > span.txt_issue > a')

sil_time = []
for i, d in enumerate(data, 1): # 이뉴머레이트 둘쨋번째에 숫자쓰면 그거부터 시작
    # sil_time[str(i) + '위'] = d.text
    rank_dict = {
        'rank': f'{i}위',
        'value': d.text
    }
    sil_time.append(rank_dict)


# csv_sil_time = open('sil_time.csv', 'w', encoding ='utf-8', newline = '')
# csv_sil = csv.writer(csv_sil_time)

# for key, val in sil_time.items():
#     csv_sil.writerow([key, val])

# csv_sil_time.close()

with open('ranking.csv', 'w', encoding='utf-8', newline='') as csvfile:
    # csv_writer = csv.writer(csvfile)
    fieldnames = ['rank', 'value']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for rank in sil_time:
        csv_writer.writerow(rank)
        # csv_writer.writerow([key, val])
# with를 하면은 close을 안해줘도 돼
 