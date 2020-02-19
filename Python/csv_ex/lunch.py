import csv

lunch = {
    '그릴스' : '매운돈까스',
    '소반' : '낙곱새',
}
# 근데 지금 문제점이 있어 한글이 안써지고이럴때>> 파일 open에 encoding = utf-8
# 헬로와 하이 사이에 공백이 들어가!>> newline = '' 기본설정은 \n이야

#<1번방법>
# csvfile = open('lunch.csv', 'w', encoding = 'utf-8', newline = '') # csv파일 없으면 자동으로 생성해줭~
# csv_writer = csv.writer(csvfile)

# for key, val in lunch.items():
#     csv_writer.writerow([key, val])

# csvfile.close()

#<2번방법>
with open('lunch.csv', 'w', encoding = 'utf-8', newline = '') as csvfile: # csv파일 없으면 자동으로 생성해줭~
    csv_writer = csv.writer(csvfile)

    for key, val in lunch.items():
        csv_writer.writerow([key, val])
