# HTML/CSS 200313

### 포지셔닝

`position: static;` 기본 설정

> 포지셔닝이 안 된 요소

`position: relative` 이렇게 바꿔주면 inline속성의 위치(원래자리를 기준으로)를 바꿔줄 수 있음!

> 여기서 `top, left, right, bottom`등 속성을 입히면 기존 위치에서 자신만 옮길 수 있어(이때, 방향은 움직이는 좌표가 아니라 내가 밀어내는 곳(여백이 생겨)) 이때, `margin`과 다른점은 마진은 다른 영향도 움직여 버린다는 것~
>
> 여기서 많이 움직이면 내가 있던 곳은 뻥 뚫림

`position: fixed` 브라우저를 기준으로 (왼쪽 위)에서 절대 움직이지 않음 즉, 스크롤을 움직여도 같아!

> 여기는 글이 아예 사라져! 내가 있던 위치에서

`position: absolute`가장 가까운 포지셔닝이 된 조상(Ancestor)요소가 기준임!!! 즉 조상요소의 공간에서 움직이게 됨!



### Float

![image-20200313130053044](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313130053044.png)

> 띄우는것!!!!!!!
>
> ![image-20200313130332554](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313130332554.png)

> 왜 이렇게 되냐?! float공간에는 inline요소가 갈수 없음 근데 글 자체는 서로 붙어있기 때문에 기본적으로 inline요소라서 float공간에 갈 수 없음
>
> 이때, 사진과 글 사이에 여백을 주고 싶으면 사진에 마진을 주면 됨

![image-20200313131458515](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313131458515.png)

> 2개를 띄웠을 때!

![image-20200313131523724](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313131523724.png)

> 같은 방향으로 했을 때

![image-20200313131608643](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313131608643.png)

> 이걸로 그리드 레이아웃을 만들 수 있어!!!

#### clear

`clear: 방향`방향에 떠있는 요소가 없도록 해주는 것

![image-20200313135700448](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313135700448.png)

> clear를 안하면 다 밑으로 깔리고 세로길이를 인식 못하게 됨. 따라서 clear: left를 해줘야함.



### List

##### `<ol>`태그 ordered list

##### `<li>`태그 list item

![image-20200313143244302](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313143244302.png)![image-20200313143252648](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313143252648.png)

> 이렇게 하면 순서를 메길 수 있음!
>
> 물론 다양한 속성으로 순서메기기 가능
>
> `<ol type='A,a,I,i,1'>` 1은 default

##### `<ul>`태그 unordered list

![image-20200313143523692](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200313143523692.png)

> 순서없어!

> style 속성바꾸기
>
> ```css
> li {
>     list-style-type: square;
>     list-style: none;
>     margin-bottom: 10px;
>     padding: 10px 20px
> }
> 
> ul {
>     padding-left: 0;
>     width: 200px;
> }
> ```