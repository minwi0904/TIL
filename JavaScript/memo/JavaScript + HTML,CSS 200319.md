# JavaScript + HTML,CSS 200319

```javascript
<a onclick="document.getElementById('photo').src = 'images/seoul.png';">Seoul</a>

<img id='photo' src='images/home.png' width='90%'>
```

> document:현재페이지
>
> getElementById('') : ''id를 통해 요소를 찾아라
>
> src = '주소'

#### 코드줄이기

```javascript
//사진 바꿔주는 함수
function clickSeoul() {
    document.getElementById('photo').src = 'images/seoul.png'
}
<a onclick="clickSeoul();">
```



