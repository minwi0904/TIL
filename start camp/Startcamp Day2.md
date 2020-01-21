# Startcamp Day2 2020.01.16



posts = ['1번글','2번글','3번글']

``` python
for post in posts
```



> posts(복수)라는 범위 안에서 post(단수)를 불러오기

for i in posts



IDLE

```python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('파이썬')
파이썬
>>> import webbrowser
>>> webbrowser.open('www.naver.com')
True
>>> webbrowser.open_new('www.google.com')
True
>>> webbrowser.open_new_tab('www.daum.net')
True
>>> url = 'https://search.naver.com/search.naver?query='
>>> keywords = ['아이유', '박신혜', '위너', 'ITZY', 'BTS']
>>> for keyword in keywords:
	print(keyword)

아이유
박신혜
위너
ITZY
BTS
>>> 
>>> for keyword in keywords:
	webbrowser.open(url + keyword)

	
True
True
True
True
True
>>> 
```

----vs스튜디오

컨트롤+`=터미널

ls= 리스트의 약자 지금 폴더의 리스트좀 보여줘

<>객체 가 담긴 큰 덩어리

BeautifulSoup = 문서 이쁘게(검색하기 편하게) 만들어줘

.select(seletor)

f12 개발자 도구



### crwaling

```python
import requests
from bs4 import BeautifulSoup

sise_url = 'https://finance.naver.com/sise/'

res = requests.get(sise_url).text
soup = BeautifulSoup(res, 'html.parser')
#KOSPI_now - 카피- 카피셀렉터로 가져온값(크롬)

kospi = soup.select_one('#KOSPI_now')
# #코스피의 샵은 아이디라는 의미
print(kospi.text)
```

> 어떤 홈페이지에서 내가 원하는 값을 가져오는 파일



### HTML

```html
<!DOCTYPE html>
<html>
    <head>
        <title>여기는 html실습을 위한 페이지입니다.</title>
    </head>
    <body>
        <h1>HTML!!!</h1>
        <h2>조금 작은 글씨입니다.</h2>
        <h6>6이 있나?</h6>

        <ul>
            <li>안녕하세요</li>
            <li>반갑습니다</li>
        </ul>

        <ol>
            <li>첫번째</li>
            <li>두번째</li>
        </ol>
        
        <a href="http://www.naver.com">네이버</a>

<!--여기는 주석입니다.-->

    </body>
</html>
```

> 홈페이지 만들기





### FLASK

ls=현재위치가 어디야?

cd= 폴더로 들어가기 체인지 디렉터



```python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

```python
from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return '반갑습니다'


@app.route('/html_tag')
def html_tag():
    return '<h1>헤딩1번입니다.</h1>'

@app.route('/first')
def first():
    return render_template('hello.html')

@app.route('/name/<string:name>')
def name(name):
    return render_template('name.html', html_name=name)

@app.route('/cube/<int:num>')
def cube(num):
    cube_num = num**4
    return render_template('cube.html', num=num, cube_num=cube_num)

@app.route('/lunch')
def lunch():
    menu = ['라면', '닭갈비', '낙지볶음밥', '오므라이스', '조기매운탕']
    menu_dict = {
        '라면': 'http://img.hankyung.com/photo/201902/AA.19048482.1.jpg',
        '닭갈비': 'http://img2.tmon.kr/cdn3/deals/2019/08/26/2370430098/2370430098_front_iJ60LlMHYy.jpg',
        '낙지볶음밥': 'https://stimg.emart.com:448/upload/peacock/item/20170906_1151019_015.jpg',
        '오므라이스': 'http://recipe1.ezmember.co.kr/cache/recipe/2019/05/20/95cc2e574065ea14d33b8397a9cb4be11.jpg',
        '조기매운탕':'https://t1.daumcdn.net/cfile/tistory/157846554D337D5135',
    }
    pick = random.choice(menu)
    img = menu_dict[pick]
    return render_template('lunch.html', pick=pick, img=img)


@app.route('/movies')
def movies():
    movies = ['해치지않아','닥터두리틀','나쁜녀석들']
    return render_template('movies.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    location = request.args.get('location')
    return render_template('pong.html', location=location)

@app.route('/god')
def god():
    return render_template('god.html')

@app.route('/result')
def result():
    source = ['라면', '닭갈비', '낙지볶음밥', '오므라이스', '조기매운탕']
    source_dict = {
        '라면': 'http://img.hankyung.com/photo/201902/AA.19048482.1.jpg',
        '닭갈비': 'http://img2.tmon.kr/cdn3/deals/2019/08/26/2370430098/2370430098_front_iJ60LlMHYy.jpg',
        '낙지볶음밥': 'https://stimg.emart.com:448/upload/peacock/item/20170906_1151019_015.jpg',
        '오므라이스': 'http://recipe1.ezmember.co.kr/cache/recipe/2019/05/20/95cc2e574065ea14d33b8397a9cb4be11.jpg',
        '조기매운탕':'https://t1.daumcdn.net/cfile/tistory/157846554D337D5135',
    }
    source_making=random.choice(source)
    src_making=random.choice(source)
    picture = source_dict[source_making]
    photo = source_dict[src_making]
    
    return render_template('result.html', source_making=source_making, src_making=src_making, picture=picture, photo=photo)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return '안녕하세요, {escape(name)}!'    

if __name__ == '__main__':
    app.run(debug=True)    
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<form action="/result">
   너의 이름은???? : <input name = "your_name">
   <input type = "submit">

</form>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>result</h1>
    <h1>when god makes you!</h1>
    <h2>{{source_making}} + {{src_making}}</h2>
    <img src = "{{picture}}" width="300" height="300"><h1>+</h1><img src = "{{photo}}" width="300", height="300">
</body>
</html>
```

