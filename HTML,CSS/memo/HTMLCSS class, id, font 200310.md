

### HTML요소에게 '이름' 주기

### 1. class 사용하기

> 클래스는 일종의 이름 같은 것
>
> ![image-20200310091719562](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310091719562.png)

> 세 번째 문단만 파랑색으로 키우고 싶을 때, 세 번째 문단에 class로 'big-blue-text'라는 이름을 지어줌 그리고 스타일에서 적용시켜주기
>
> 이때, class라고 표시해주기 위해선 이름앞에 `.`을 붙임

> 2가지를 적용시키고 싶을 때, 클래스 이름에 한칸 띄고 이름 또 써주면 됨.
>
> ![image-20200310092003130](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310092003130.png)

> 클래스를 사용하면 여러요소에게 동일한 스타일을 적용하고 한 요소에게 다양한 스타일을 적용시킬 수 있음



### 2. id 사용하기

가장 좋아하는 문단 표시로 id에 이름 정해주기

![image-20200310092158209](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310092158209.png)

`< p id='best-text'>첫번째 문단</p>`

> 똑같이 스타일에서 적용시켜줌
>
> 이때, id라고 표시해주기 위해선 이름앞에 `#`을 붙임

![image-20200310092401616](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310092401616.png)



#### class 와 id의 차이????

1. 중복 여부

- class는 중복 클래스 가능
- id는 중복 아이디 불가능(각 페이지에서 중복되는 id있으면 안됨)

![image-20200310092626915](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310092626915.png)

2. 중첩 여부

- class는 한 요소가 여러 클래스를 가질 수 있음
- id는 한 요소가 여러 클래스를 가질 수 없어

![image-20200310092904812](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310092904812.png)

> 클래스는 문단 1이 big클래스와 blue클래스 둘 다 가질 수 있지만,
>
> id는 문단 1이 best아이디와 first아이드를 둘 다 가질 수 없고, 하나만 가질 수 있음.
>
> > + 추가로 한 요소가 여러 클래스를 가지고 아이디도 하나 가질 수 있다!



> > 언제 사용해야할까?
> >
> > ![image-20200310093033019](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310093033019.png)
> >
> > ![image-20200310093047061](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310093047061.png)



### `<div> `태그

> 묶어주고 싶은 태그를 <div>태그로 감쌈

> div에 클래스 주면 묶어준 친구들을 일관성있게 스타일을 입혀줄 수 있음.



### CSS 파일 따로 쓰기/link로 연결

![image-20200310100742403](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310100742403.png)

css폴더에 styles.css 파일 만들고

`    <link href="css/styles.css" rel='styleheet'>`

연결 시키기 , 이때, rel은 relation의 준말

> 다른 방법!  style 속성
>
> `<h1 style="color: red; font-size: 72;">코드잇</h1>`

> 가장 추천하는방법은 외부 css파일 쓰고 link로 연결하는게 제일 좋음
>
> 1. 파일 각각에 역할이 확실히 있는 게 좋음! 길어지면 지저분해짐
> 2. 외부파일 사용하면 깔끔하게 표현할 수 있음, 수정도 쉬움
>
> but, style 속성이 좋을 때는 어떤게 좋을지 테스트 할 때 추천!, 바로바로 가시적으로 확인할 수 있어, css파일 수정하면 귀찮아
>
> 아무튼 결국엔 모두 외부파일로 옮길 거지만 테스트할 때는 html파일에 써보고 옮기기~~~



#### 주석달기

* html 주석: `<!-- 내용 -->`
* 단축키 : ctrl + /(여러줄일땐 ctrl + shift + /)

> 사용하는 이유 > 코드가 길어지면 길어질 수 록 알아보기 힘들어지고 헷갈려, 따라서 설명을 써주면서 여기가 어떤건지 알 수 있음

- css 주석: `/* 내용 */`
- 단축키:  ctrl + /(여러줄일땐 ctrl + shift + /)



#### 유용한 사이트

1. 구글 >> 영어로 검색하는게 좋음.
2. stack overflow
3. jsfiddle(html, css, javasctipt한꺼번에 바로 실행해서 결과를 손쉽게 알 수 있음) >> 질문을 할때, 이거를 사용하면 훨씬 편함



### 텍스트 스타일링

#### 색깔

1. 직관적으로 색깔이름 써주기

```html
<style>
    h1 {
        color: blue;
    }
</style>
```

2. CSS전용 색명칭 사용 : 140개 색이 지원
3. html color codes라는 사이트로 가면 모든 색을 사용가능함>>색깔 코드를 갖고옴 

![image-20200310105604806](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310105604806.png)

4. HEX값 사용 ex)#00ff00이런거 있짠헝(16진법으로 표현)

![image-20200310105807173](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310105807173.png)

#### 굵기

`font-weight`: 100~900까지 값 사용가능 100이 가장 얇은 것

> 400이 보통 굵기, 700이 <b>사용한 것과 같은 느낌
>
> 조심할 것은 단위가 100이라서 110이런 값은 없어.
>
> > 폰트마다 지원하는 굵기가 다달라서 테스트 해봐야함.



#### 정렬

`text-align`: center, left, right

> 그런데, h1이나 p는 화면 전체를 차지하는데 a태그는 글자그부분만 차지해서 center가 안됨
>
> 이럴때는 a태그를 div로 감싸주면 화면 전체를 차지할 수 있게함!> 이러면 div한테 속성을 주면 center가 먹힘.



#### 꾸미기

`text-decoration: 내용;  ` (a태그에 많이 사용함>하이퍼링크 밑줄 싫을때)

- underline : 밑줄치기
- overlin: 글 위에 밑줄치기
- line-through: 글 가운데 줄치기 
- none : 밑줄 없애줌(꾸밈 없애줌!!!!!!)



#### 크기

폰트 사이즈 나누기

- 절대적 : px, pt >> 어떤요소에도 영향을 받지않고 그 크기 그대로 나옴

  > 여기서 px*1.33배 정도 == pt(웹에선 pt잘 안쓰임)

- 상대적 : em, %  >> 기준 값 (부모한테 영향받음)이 있으면 그 기준을 따라서 크기가 커지고 줄어들고 함.

![image-20200310111935254](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310111935254.png)

![image-20200310111959294](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310111959294.png)

> body가 16픽셀
>
> div1의 부모는 body이므로 16px(100%), 같은 방식으로 div2는 부모가 div1이므로 32픽셀, div3는 64px
>
> 1em == 100%, 2em, == 200%, 1.5em == 150%



#### 줄간격

`line-height`

![image-20200310112351778](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310112351778.png)

> `line-height`를 통해서는 각 줄이 실질적으로 차지하는 공간을 정해줄 수 있습니다. 예를 들어서 `99px`로 설정하면 'content area'보다 `40px`이 많기 때문에 위 아래로 `20px`의 공간이 추가로 생깁니다.
>
> 반대로 `40px`로 설정하면 'content area'보다 `19px`이 적기 때문에 위 아래로 `-9.5px`의 공간이 줄어듭니다.



#### 폰트 설정

<폰트종류 5가지>

1. serif  : 끝에가 꼬부랑
2. sans-serif : 깔끔한 디자인
3. monospace : 모든 글자폭이 똑같음, 그래서프로그래밍 용으로 많이 쓰임
4. cursive : 필기체 
5. Fantasy: 특이한 나머지 글꼴

![image-20200310112700987](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310112700987.png)

##### 사용방법1(폰트가 설치돼있을 때)

`font-family: 내용;`

- 글꼴 이름 쓰면 돼 ex) 'Times New Roman'

> 근데, 컴퓨터에 글꼴이 있어야지 잘나옴

- 폰트 우선순위 ex) 'Times New Roman', 'Times', '폰트종류'

> 제1글꼴, 제 2글꼴, 최후의 수단 글꼴 순



##### 사용방법2(폰트가 설치안 돼있을 때)

> 직접 폰트파일 제공해주면 돼!

1. 구글 폰트 자주사용함(font.google.com) : 원하는 폰트 추가하고 2 familes selected >> 링크 복사

2. ![image-20200310113336004](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310113336004.png)

   <head에 넣기>, 이거는 barrio폰트와 roboto사용가능

   3.` font-family: 폰트이름, 폰트종류;`1번사용못하면 사용가능한 2번폰트 사용해라.

   ![image-20200310113602575](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310113602575.png)

> 근데, 위는 한글폰트가 없어 이럴땐,
>
> font.google.com/earlyaccess >>베타출시 폰트 페이지에서 찾기로 korean찾아서 괜찮은 폰트 사용하기! 주소부분 복사해서 사용하면 됨(위와 동일)



##### 사용방법3(내가 가진 폰트파일 사용하기)

1. 폰트파일 설치하고 폴더에 폰트파일 저장해놓기
2. css파일 작성

```css
/* 폰트 설치 */
@font-face {
    src: url('../fonts/폰트이름.otf'); # 경로설정
    font-family: '이름 설정' # 내가 폰트이름 맘대로 짓기
}
/* 폰트 사용*/
p {
    font-family: '내가 만든 폰트 이름';
}
```



#### span태그

#### `<span>` vs `<div>`

> 둘다 그냥 글을 묶어주는 용도지만 div는 줄을 바꾸는 반면 span은 원본을 건들이지 않고 묶어줌



