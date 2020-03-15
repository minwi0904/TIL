# HTML/CSS 200314

### 반응형 웹

#### 미디어 쿼리

> 브라우저 사이즈에 맞춰서 레이아웃이 알맞게 바뀌는 것!
>
> 이렇게 만들면 따로 모바일이나 타블렛버전을 안만들어됨

```css
@media (min-width: 768px) {
    h1 {
        font-size: 36px;
    }
    p {
        font-size: 24px;
    }
}
```

> 만약 브라우저의 길이가 768px부터 폰트사이즈를 저렇게 바꿔라!!!!!!!!!!!

```css
@media (min-width: 992px) {
    h1 {
        font-size: 48px;
    }
    p {
        font-size: 32px;
    }
}
```

> 이거는 브라우저가 992부터는 폰트가 또 커짐