# HTML/CSS 200312

### CSS 활용하기

> CSS에서 스타일링 해줄 요소는 '선택자'로 결정

- 태그 이름
- 클래스/아이디
- 자식(children)

```css
/* 'div1' 클래스를 갖고 있는 요소의 자식 중 모든 <i> 태그 */
.div1 i {
  color: orange;
}
```

- 직속 자식(direct children) > 몇다리 건너면 되지 않음!

```css
/* 'div1' 클래스를 갖고 있는 요소의 직속 자식 중 모든 <i> 태그 */
.div1 > i {
  color: orange;
}
```

- 복수 선택

```css
/* 'two' 클래스를 가지고 있는 태그 모두와 'four' 클래스를 가지고 있는 태그 모두 선택 */
.two, .four {
  color: orange;
}
```

- 여러조건

```css
/* 'outside' 클래스를 갖고 있으면서 'one' 클래스도 갖고 있는 태그 */
.outside.one {
  color: blue;
}

/* 'inside' 클래스를 갖고 있으면서 'two' 클래스도 갖고 있는 태그 */
.inside.two {
  color: orange;
}
```

- Pseudo-class(가상 클래스)

  1. n번째 자식

  ```css
  /* .div1의 자식인 <p> 태그 중 3번째 */
  .div1 p:nth-child(3) {
    color: blue;
  }
  
  /* .div1의 자식인 <p> 태그 중 첫 번째 */
  .div1 p:first-child {
    color: red;
  }
  
  /* .div1의 자식인 <p> 태그 중 마지막 */
  .div1 p:last-child {
    color: green;
  }
  
  /* .div1의 자식 중 마지막 자식이 아닌 <p> 태그 */
  .div1 p:not(:last-child) {
    font-size: 150%;
  }
  
  /* .div1의 자식 중 첫 번째 자식이 아닌 <p> 태그 */
  .div1 p:not(:first-child) {
    text-decoration: line-through;
  }
  ```

  2. 마우스 오버 (hover)

  ```css
  /* 마우스가 <h1> 태그에 올라갔을 때 */
  h1:hover {
    color: green;
  }
  ```

  

#### CSS 상속

> class(요소들 속성)안에 속해 있으면(자식들이라면), 설정이 이어짐 = 부모 요소 속성이 자식에게  상속됐기 때문

> 하지만 안되는 것도 몇가지 있음
>
> **대부분 상속되는 것들**
>
> - color
> - font-family
> - font-size
> - font-weight
> - line-height
> - list-style
> - text-align
> - visivility
>
> > but, 이친구들도 항상 상속되는 것이 아님. 특히 <a>태그에는 color속성이 적용되지 않는데, 이때 상속을 받아오려면 inherit값을 써야함
> >
> > ```css
> > .div2 {
> >   color: orange;
> > }
> > 
> > .div2 a {
> >   color: inherit;
> > } # 이렇게!
> > ```



#### CSS 우선 순위

> 여러 선택자가 같은 요소를 가리킬 때의 우선순위!

##### 1. 순서

> 완전 똑같은 선택자가 css파일에 다시 쓰여진다면 덮어쓰기가 됨(중복되는 스타일만)

##### 2. 명시도(Specificity)

> 같은 요소를 가르키지만 선택자가 다르다면 '명시도'에 따라 우선 순위가 결정됨

###### > 명시도 계산기

>1. 인라인 스타일이 가장 큰 우선순위
>2. 선택자에 id가 많을 수록 큰 우선순위
>3. 선택자에 class, attribute, pseudo-class가 많을 수록 우선 순위
>4. 그냥 요소(or 가상 요소)가 많은 순서

![image-20200312105729871](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312105729871.png)

> 각 자리는 1000의자리, 100의 자리, 10의 자리, 1의 자리
>
> 첫 번째 경우에는 일반 요소가 세 개, 가상 클래스가 한 개 있어서 '명시도 점수'가 13입니다. 두 번째 경우에는 일반 요소가 두 개, 가상 클래스가 한 개, 그리고 id가 한 개 있어서 112점입니다.

> 따라서, CSS파일에 위와 같은 선택자가 입력돼있으면 2번째 선택자의 스타일이 적용됨



#### CSS 단위

###### PX

> 절대적인 값, 다른 요소의 값에 영향을 받지 않음

###### rem

> 상대적인 값, 오직 <html>태그의 font-size에만 영향을 받음
>
> ``` css
> html {
>   font-size: 20px;
> }
> 
> .container {
>   padding-top: 2rem; /* html의 font-size * 2 = 40px */
>   background-color: lime;
> }
> ```

###### em

> 상대적인 값, em은 자기 자신의 font-size를 기준으로함
>
> 자기 자신 font-size정해주지 않았을 경우, 상위 요소에서 상속받은 값을 기준으로 함.
>
> ```css
> .container {
>   font-size: 40px;
>   padding-top: 2em; /* 자신의 font-size * 2 = 80px */
>   background-color: lime;
> }
> ```

###### 퍼센트(%)

> 상대적인 값, 어느 항목에서 쓰이냐에 따라 다른 기준 적용
>
> ex) font-size에서 %쓰일 때, 상위 요소 font-size에 곱해줌
>
> ex)margin이나 padding에서 사용될땐, 상위 요소 width에 곱해줌, 근데 margin-top이나 padding-bottom 등 세로(상하) 속성을 조절할 때도, width를 기준으로 함.



### Display 속성

> 대부분 2가지 중 하나를 가지고 있음!

![image-20200312112631698](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312112631698.png)

#### < inline display >

![image-20200312112702065](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312112702065.png)

#### < block display >

![image-20200312112820633](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312112820633.png)

> 자, 이제 속성을 바꿔보자
>
> ![image-20200312113042330](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312113042330.png)
>
> i는 inline이라서 딱 필요한 만큼만 차지하는데 이렇게 해주면, block display속성를 가져서 공간을 가능한 한 많이 차지해서 다음 줄로 넘어감, 반대도 가능!! `display: inline;`

<display 종류>

1. inline display

   - `<span>`, `<a>`, `<b>`, `<i>`, `<img>`, `button`

   - 이친구들은 width와 height를 설정해도 안됨, 왜냐면 가로길이 세로길이가 없고 내용물에 따라서 바뀌는 것일뿐..!

     > 그래도 바꾸고 싶을 땐, inline-block을 설정하자 3번에서 계속

2. block display

   - `<div>`, `<h1>~<h6>`, `<p>`, `<nav>`, `<ul>`, `<li>`
   - 이친구들도 width와 height로 가로, 세로 설정 가능함!

3.  inline-block

> ![image-20200312114158722](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312114158722.png)
>
> inline을 display: inline-block으로 바꿔주니 크기 설정 가능해짐!
>
> 같은줄+가로세로까지 가능한게 inline-block display!

4. flex

5. list-item
6. none



#### `<img>` 태그 비밀

> 텍스트와 같은 줄 + 가로세로 설정가능이지만 inline-block이 아니고 실제는 inline 요소임
>
> 이 친구는 텍스트 취급이 가능함>> 엄청 큰 글자라고 생각하자
>
> 따라서, 글자속성을 그대로 가져갈 수 있어.
>
> 그치만 주로 이미지 가운데 정렬 해줄 때는, 
>
> ![image-20200312114752601](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312114752601.png) 
>
> 이거 써줌



#### 링크

> 사진으로도 링크 가능함
>
> ![image-20200312114932555](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312114932555.png)

> ![image-20200312115221314](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312115221314.png)![image-20200312115208667](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312115208667.png)
>
> 이 이미지도 링크를 걸고 싶을때는?
>
> div class를 a class로 바꾸면 됨!
>
> ![image-20200312115354119](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312115354119.png)



### Baseline

![image-20200312122159990](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312122159990.png)

![image-20200312122227252](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312122227252.png)

>  기본적으로 텍스트는 보이지 않는 베이스라인에 맞춰져 있음

![image-20200312122356430](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312122356430.png)

>  일반적으로 이렇게 중복돼서 글이 써질때는 디브 마지막 요소가 베이스라인이 돼서 alex와 chris가 맞춰진것, 그렇지만 예외가 존재함
>
> 1. 인라인 블록 요소안에 글이 하나도 없을때 베이스 라인은 박스밑변이 베이스라인이 됨
>
>    ![image-20200312122527366](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312122527366.png)
>
> 2. 인라인요소 크기를 줄여도 크리스가 마지막줄이어서 베이스라인이 크리스가 됨, 근데 오버플로우 속성이 비지블이 아닌 것을 설정해주면 베이스라인이 바뀜!
>
>    ![image-20200312122647427](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312122647427.png)



#### vertical-align

> baseline 기본설정은 부모요소의 vertical-align!!
>
> ![image-20200312122957219](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312122957219.png)

> 이때, ben 속성을 `vertical-align: top;`을 하면 가장 높이올라간 속성위에 맞춰짐![image-20200312123114189](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312123114189.png)

> 만약, 알렉스에 vertical-align:top을 한다면?
>
> ![image-20200312123247826](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312123247826.png)
>
> 전부 움직임...왜그러냐?@
>
> 1. 크리스가 올라가고 크리스 베이스라인에 나머지 베이스라인이 맞춰짐
> 2. 이때, baseline은 verrical-align 조건들을 충족시키면서 줄의 높이를 최소화시키는 곳에 위치

> 미들을 할때는?!
>
> 부모태그의 가운데와 어떤 요소의 가운데가 맞춰짐



#### 가로 가운데 정렬

![image-20200312124143629](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312124143629.png)

![image-20200312124154666](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312124154666.png)

#### 세로 가운데 정렬

> 이건 여러과정을 거쳐야함(너무 복잡..)
>
> ![image-20200312124456127](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200312124456127.png)
>
> 1. x를 적고(부모), vertical-align: middle 설정 후, 이 x가로길이를 보여줄 가짜 박스 높이를 100%바꾸면 x가 정 가운데 오게 됨, 동시에 초록박스도!, 이제 x를 지우고 , 가짜박스도 지우기
> 2. 자세한건 vs코드 참고