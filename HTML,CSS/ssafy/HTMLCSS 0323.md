













# HTML/CSS 0323

#### flex

- `flex`이전에는 배치를 위해서 `float`, `position`으로 지정을 해야했다.

주요개념

1. `container`, `item`

```css
<style>
.container {
    display: flex;
}
</style>
<div class= 'container'>
	<div class= 'item'></div>
</div>
```

2. `main axis`, `cross axis`
3. `flex`정의시 
   - `main axis`을 기준으로 배치가 시작된다.
     - 만약, row-reverse설정하면 오른쪽위부터 채워짐
   - 모든 `item`은 행으로 배치된다.(`flex-direction: row`(default))
   - 모든 `item`은 `cross axis`을 모두 채운다.
   - 모든 `itme`은 본인의 너비 혹은 컨텐츠 영역만큼 너비를 가지게 된다.
     - 경우에 따라서, 본인이 지정받은 너비보다 작을 수 있다.

![image-20200323100115100](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200323100115100.png)



> 여기서 `column-reverse`를 하면 main축이 위에서 아래로가 아니라 아래에서 위로 배치

![image-20200323100333093](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200323100333093.png)









