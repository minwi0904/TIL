# HTML/CSS 200309

> html은 페이지 내용을 담고 css는 디자인을 담당

```html
<!DOCTYPE html>

<html>
<head>
    <title>My First Website</title>
    <meta charset='utf-8'>
    <!--콜론 뒤에 띄어쓰기, 세미콜론 필수-->
<style> 
    h1 {
        font-size: 64px; 
        text-align: center;
    }

    h3 {
        margin-top: 100px;
    }

    p i { 
        font-size: 48px;
    }
</style>
<!--이러면 p태그 안에 있는 i태그만 한다 p안적으면 love도 커짐-->
</head>

<body>
<h1>My First Page</h1>
<h2>I <i>love</i> HTML!</h2>
<h3>안녕 세상!</h3>

<img src='https://www.topstarnews.net/news/photo/202002/730543_448926_4616.png' width='300'>
<img src='images/12330788-무지개의-색깔에-아이스크림.jpg' width='300'>

<p>I'm <b>minwon</b> <i>minwon</i> minwon.</p>

<a href='https://google.com' target='_blank'>구글로 가는 링크</a>

<a href="folder1/page1.html">page 1</a>
<a href="folder1/folder2/page2.html">page 2</a>

</body>
</html>
```

`<b></b>`  : 굵게

`<strong></strong>`: 감싸고 있는 텍스트가 중요하다고 표시하는 것이 목적 > b와 겉보기는 같지만 장애인용 웹을 만든다거나할때 강조해서 읽을 수 있음

`<i></i>` : 기울게

`<em></em>`: i와 같은 기능이지만 강조가 목적, em은 emphasized줄임말

한글이 깨질때 : 익스플로어 사용시 한글이 깨짐, 크롬은 안깨짐 >> 어떻게든 안깨지게 할때는 `<meta charset='utf-8'>`사용해주기



#### `<a></a>`: 하이퍼링크 태그(anchor)

> `<a href='가고 싶은 주소'> 내용 </a>`

![image-20200310001933459](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310001933459.png)

> <a href='https://google.com' target='_blank'>구글로 가는 링크</a>
>
> target='_blank'새창으로 열기, 안하면 원래창에서 바뀜
>
> ```html
> <a href='../../index.html'>index</a> 폴더 두번 타고 올라가기
> <a href='../page1.html'>page1</a>
> <a href='page3.html'>page3</a> 같은 폴더 내 이동
> ```



#### 이미지 넣기

`<img src='주소' width/height='숫자'(하나만 넣으면 비율대로 바뀌지만 둘다 넣으면 다 바뀜)>`

> img태그에 src라는 속성을 갖음, 종료태그 없음
>
> 이미지 가운데 정렬 하고 싶을 때
>
> ![image-20200310004342881](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310004342881.png)



#### CSS 기본 문법

![image-20200309235240085](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200309235240085.png)

```html
<style> 
    h1 {
        font-size: 64px; # 폰트크기 표현 단위px이 가장 많이 사용
        text-align: center; # 가운데 정렬, left, right 사용가능
        color: hotpink; # 색깔입히기
    }
    h3 {
        margin-top: 100px; # 여백주기(위), bottom, left 등 사용가능
    }
    p i { 
        font-size: 48px;
    }
</style>
```

