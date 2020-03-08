import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요.
records = []

for year in range(2010, 2019):
    month = 1
    for month in range(1, 13):
        weekindex = 0

        week = True
        while week:
            response = requests.get('https://workey.codeit.kr/ratings/index?year=' + str(year) + '&month=' + str(
                month) + '&weekIndex=' + str(weekindex))
            soup = BeautifulSoup(response.text, 'html.parser')

            # "row" 클래스가 있을 때만 상품 정보 가져오기
            if len(soup.select('.row')) > 2:
                period = soup.select('#weekSelectBox')
                rank = soup.select('.rank')
                channel = soup.select('.channel')
                program = soup.select('.program')
                rating = soup.select('.percent')
                weekindex += 1

                period = period[0].text.split('\n')[1: -1]

                for week in period:
                    index = 1

                    for i in range(len(rank)-1):
                        record = []
                        record.append(week)
                        record.append(rank[index].text)
                        record.append(channel[index].text)
                        record.append(program[index].text)
                        record.append(rating[index].text)
                        records.append(record)
                        index += 1
            else:
                week = False

print(records)
# df = pd.DataFrame(data = records, columns = ['period', 'rank', 'channel', 'program', 'rating'])

# 결과 출력
# df.head()