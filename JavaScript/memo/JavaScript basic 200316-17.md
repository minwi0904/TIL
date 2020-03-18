# JavaScript 200316,18

### 코멘트

```javascript
// alert('Hello Codeit~!')

/*
안녕하세요
안녕하세요
안녕하세요
*/
```

> 주석처리는 슬래시 슬래시
>
> or CSS랑 같은 /* */



#### 변수(Variable) & 상수(Constant)

```java
<script>
    var score = 0; //모든 자바스크립트는 세미콜론으로 끝냄
</script>
```

> 변수 선언 `var, 이름설정 = 초기값설정;`

```javascript
// 변수만 선언하고 값은 나중에 주고 싶으면
var score;
score = 0;
```

```javascript
//변수 여러개 만들고 싶을때
var score = 1, score2 = 0;

//변수 이름
var 1player; //오류, 처음에 숫자가 올수 없음
var player^1; // 오류, 특수문자는 사용가능한 것만
```

```javascript
//상수 선언
const MAX_LEVEL = 99;
```

> `const 상수 이름 = 상수;`
>
> 상수는 못바꿈

----------

<지켜야하는 룰>

1. JavaScript 식별자는 '문자(a-z, A-Z)', '밑줄(_)', '달러($)'로만 시작, 두번째부터는 숫자도 가능

2. 대소문자를 구별하기 때문에 서로 다르게 인식됨.
3. 예약어

<지키면 좋은 룰>

1. 의미없는 이름 X
2. 추상적 이름 X
3. 변수는 camelCase로 쓰자



### 데이터 타입

1. 숫자형
2. 문자형
3. 논리형

```javascript
// 타입알아보기
typeof 변수;
>> 'number', 'string', 'boolean'
```

------------

> 숫자연산은 파이썬과 비슷함. 그런데 javascript는 소수와 정수를 구별하지 않고 전부 number로 취급

> 문자형도 파이썬과 비슷함. `'', ""` 모두 사용가능함.
>
> 문자열 연산은 서로 연결돼서 붙이기

> boolean형, ture, false, 
>
> > javascript에서 같다(`==, ===`)
> >
> > - ==는 데이터타입이 달라도 값이 같으면 True
> > - ===는 데이터타입이 다르면 값이 같아도 False(앤 둘 다 같아야 True)
> >
> > and연산(`&&`)
> >
> > or연산(`||`)
> >
> > not연산(`!`)



#### Syntactic Sugar

> 파이썬에서 `+=, -=, *=, /=, %=`과 사용하는 것과 동일
>
> 추가로 변수의 값을 1씩 증감시킬 때 사용하는 문법도 있음
>
> ```javascript
> x += 1; == x++;
> x -+ 1; == x--;
> ```



#### 형변환

``` javascript
var scoreString = '10';
number(scoreString)
>> 10
typeof scoreString
>>'string'
```

> 문자열로 바꾸기 `String(변수)`



### 배열(Array)

```javascript
var brands = ['Apple', 'Coca-Cola', 'Starbucks'];
var iPad = [800, 'Black', true]; // 다양한 자료형도 담을 수 있음
```

> `tpyeof brads;`>>object로 나옴!!
>
> 꺼내서 쓰는법(인덱싱하면 됨)>> 파이썬과 같음

#### 2차 배열

```javascript
var products = [
    ['iPhone', 'iMac', 'Macbook'], 
    ['Coke', 'Diet Coke'],
    ['Americano', 'Latte', 'Tea'],
];
```



### 객체

```javascript
var person = ['Dongwook', 30, 'Korea'];
console.log(person[2]) // 국적을 받아 올 수 있음
// 근데 이렇게 하면 어디에 뭐가 있는지 알아야함.
// 많아지면 헷갈리잖어, 이때 필요한건?
var person = {
    name: 'Dongwook',
    age: 30,
    nationality: 'Korea'
};
//이렇게 하면 ?
console.log(person['nationality']);
==console.log(person.nationality) //위와 같은 표현임!
>> Korea
```



### 함수

```javascript
function logTask(task) { //함수만들기
    console.log(task + ': 완료');
    console.log('-');
}
logTask('보고서 작성'); //함수실행
```

#### 내장함수

###### 형변환함수

`String(숫자형변수)` : 문자로 변환

`Number('문자형변수') `: 숫자형으로 변환

`parseInt('숫자' + '문자')`: 숫자만 꺼내서 숫자로 변환

> 주의할 것은 숫자가 앞에 와야함

`parseFloat('숫자'+'문자')`: 문자열 안에서 숫자(소수 포함)을 뽑아서 숫자로 변환

###### 기타 함수

`alert()`: 사용자에게 메시지를 띄워주는 함수

`prompt()`: 사용자에게 메시지를 띄우고, 문자열을 입력받는 함수

`confirm()`: 사용자에게 메시지를 띄우고, 확인과 취소 중 하나를 누르게 하는 함수



### 조건문(if)

```javascript
window.prompt('한 자리 숫자를 적어주세요.');

console.log(inputNumber); // 콘솔에 출력하는 함수
// 문자열 7인지 확인하는 법
if (inputNumber === '7') {
    alert('Lucky'!);
} else if (inputNumber === '0') {
    alert('Zero');
} else if (inputNumber === '1') {
    alert('One');
} else {
    alert('Unlucky!');
}
```

``` javascript
var num;
if (num % 2 === 0 && num % 3 === 0) {
    console.log(num + '는 6의 배수입니다.');
} else {
    console.log(num + '는 6의 배수가 아닙니다.');
} //근데 애는 정수랑 문자형도 서로 연산이 되네??
```



#### Switch문

```javascript
var inputNumber = window.prompt('한 자리 숫자를 적어주세요.');

switch (inputNumber) {
    case '0':
        alert('Zero!');
    	break; //switch문에서 빠져나와서 아래는 다 무시해라
    case '1':
        alert('One!');
    	break;
    case '7':
        alert('Lucky!');
        break;
    default:
        alert('Unlucky!');
        break;
}
```

> break를 넣지않으면 계속 다음케이스로 넘어감!

> **if와 switch의 차이는 뭘까**
>
> ```javascript
> var score = 85;
> 
> if (score > 70) {
>     alert('잘 하셨습니다!');
>     } // 이렇게 끝남! 그런데 스위치 문으로 바꾸면
> ```
>
> ![image-20200316140655020](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200316140655020.png)
>
> 이렇게 100까지 써줘야함.!

> switch가 더 좋은 경우는?
>
> ![image-20200316140751319](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200316140751319.png)
>
> 범위가 아니라 개체로 딱딱 나뉘어 있을 땐, switch가 더 좋음
>
> ```javascript
> var courseName = 'A';
> switch (courseName) {
>     case 'C':
>         console.log('게살스프 칠리새우');
>     case 'B':
>         console.log('유산슬');
>     case 'A':
>         console.log('짜장면 짬뽕 탕수육 양장피 팔보채');
>         break;
>     defulat:
>         console.log('주문이 잘못되었습니다.');
>         break;
> }
> ```
>
> 이렇게 하면 중복없이 모두 나오게 할 수 있음.



### for반복문

```javascript
for (var i = 0; i < 6; i = i + 1) {
    console.log(brands[i]);
}
```

![image-20200318113747912](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200318113747912.png)

#### for of 반복문

```javascript
for (value of brands) {
    console.log(value);
} //브랜즈 원소자체를 하나 씩 가져오는거!
```

> value는 임의의 이름

#### for in 반복문 >>사용지양하기

```javascript
for (var k in arr) {
    console.log(k);
} //인덱스에 접근하기
```



### while 반복문

```javascript
var i = 0;

while (i < 6) {
    console.log(brands[i]);
    i++;
}
```

> while조건부가 true일때만 작동, 파이썬과 동일