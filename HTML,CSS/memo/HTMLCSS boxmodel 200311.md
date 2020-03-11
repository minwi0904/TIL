# HTML/CSS 200311

#### Box model

![image-20200311100631936](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200311100631936.png)

> 각 요소는 사각형으로 이루어져 있음!
>
> border을 기준으로 안 밖으로 여백 줄수있어!



#### padding 설정하기

1. 직관적인 방법`padding-top/bottom/left/right:   ;`

2. 간편방법 `padding:  top right bottom left;`

   > 시계방향으로 한칸씩 띄고 적기, 패딩이 4방향 다 같다면 한가지 값만 적어도됨, 위=아래, 오른=왼 일때는 위아래 먼저적고, 왼오적어도됨

#### margin 설정하기

> 패딩과 동일!---

---------------



> ![image-20200311101524381](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200311101524381.png)
>
> 만약, 내가 어떤 요소를 가로길이를 주면, 자동으로 왼쪽으로 쏠림 이때 가운데 정렬을 하고 싶으면 왼쪽 오른쪽 margin을 오토로 주면 됨



#### width & height

`width` `height` 

`min-width`: 이 요소의 가로 길이가 적어도 이정도는 돼야한다! 만약에 화면이 줄어들다가 어느 정도까지 줄어들면 화면 밖으로 나가짐!

> 반대 `max-width` > 어느순간부터는 화면이 늘어나도 늘어나지 않음 쉽게 생각하면 가로길이의 최대 최소를 정해줄 수 있는것!

 `min-height`

> 높이에서도 동일하게 적용됨
>
> 그런데 최대값을 설정해주고, 내용이 많아지면 박스가 커지지 않아서 overflow가 됨! 



#### overflow

> 글이 사각형밖으로 삐져나왔을때!

`overflow` : 옵션;

- hidden : 숨기기(잘림)

- visible(default) : 보이기
- scroll: 스크롤로 움직일 수 있음(내용이 적어도 항상! 스크롤바가 나옴)
- auto: 스크롤(내용 많을 때만 스크롤 바 나옴)



#### border

`border` : 숫자px(선굵기) solid(선종류) #색깔;

- solid: 실선
- dotted: 점선
- dashed: 파선
- none  or 0: 선 없애기

`border-style` ,`border-coler`, `border-width`이렇게 다 따로 쓸 수 도 있긴함.

>![image-20200311113406465](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200311113406465.png)

이렇게 선을 따로 따로 쓸 수도 있음



#### 박스 꾸미기

`border-radius`: px;

> 모서리를 둥글게 만들 수 있음
>
> `border-top-left-radius` 이렇게 네 귀퉁이 따로 설정 가능함

`background-coloer`: #색깔, rgb등등

> 원하는 곳 색칠하기

- transparent(default): 배경 투명!

`box-shadow`: 가로그림자px 세로그림자px 흐림px 크기px #색깔; (음수값도 가능함, 반대로 그림자짐)

> 그림자 넣기

- none(default): 그림자 없어



#### box-sizing

![image-20200311114922279](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200311114922279.png)![image-20200311115019546](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200311115019546.png)

이처럼 content가로길이 세로길이를 정하는데 패딩도 정하고 테두리도 정하면 크기가 380*280이됨

그래서 원하는 크기로 만들려면 width랑 height에 각각 값을 빼줘야함>> 귀찮아 이걸 설정했을 때 딱 맞춰서 나오면 좋겠어! 이때!

`box-sizing`: border-box;로 설정하자!

- content-box(default) : 테두리와 패딩은 별개로 작동
- border-box: 한꺼번에 취급됨



### +++++꿀팁

> 모든 요소에 원하는 스타일 넣고 싶을 때!

```css
* {
    box-sixing: border-box; # 이거는 요즘 모두 꼭 넣고있어
}
```



#### 배경이미지 

`background-image`: url('주소를 적어줘라, 경로를 적어줘라/그림.jpg');

`background-reqeat`: 

- no-repeat : 바둑판 정렬 X
- repeat: 바둑판 정렬
- repeat-x:가로 반복
- repeat-y:세로반복
- space: 반복할 수 있는 만큼 반복후, 남는 공간은 이미지 여분으로 배분
- round: 반복할 수 있는 만큼 반복후, 남는 공간은 이미지 확대로 배분

`background-size` : 가로px 세로px; or 100% 500px(이러면 꽉차)

> but, 항상 꽉채우면서 찌그러 지지도 않는 방법은 무엇일까?
>
> - cover(배경을 꽉채우면서도 비율을 유지시키겠다!)
>
> > 이러면 근데 사이트 크기에 따라 잘릴 수 있음
> >
> > 그래서 잘리는건 어쩔 수 없는건데 어떤곳이 잘리는지 정하고 싶어
>
> - background-position: 고정 위치; ex)right bottom(잘릴때, 오른쪽이랑 바텀은 늦게 잘림)
>
> ```css
> background-position: left top;
> background-position: left center;
> background-position: left bottom;
> background-position: right top;
> background-position: right center;
> background-position: right bottom;
> background-position: center top;
> background-position: center center;
> background-position: center bottom;
> ```
>
> 이렇게 9가지 조합 가능함
>
> %으로 지정가능, px로 지정가능



