# Python_20200217_Errors 

### Syntax Error

> 문법 에러: 가장 흔한 에러로 파일이름과 줄번호, ^문자를 통해 파이썬이 읽어 들일 때 문제 발생 위치를 표현

> 파이썬 문법을 안지켰을 때 나타남

- invalid syntax(이상한 문법)
- EOL 오류(따옴표 오류)

- EOF 오류(괄호 닫기 오류)



### Exceptions

> 예외!! 문법이나 표현식이 바르게 됐지만, 실행시 발생하는 에러

- ZeroDivisionError (0으로 나눴을 때 발생)
- NameError(없는 변수 썼거나, 변수 오타 냈을 때)
- TypeError(다른 자료형의 타입끼린 뭔가 못해, 적합하지 않은 타입으론 뭔가 못해, 필수 argument를 누락했거나, argument가 더 많았을 때 나옴.)
- ValueError(타입은 적절하지만 값이 적절하지 않을 때, 값이 없는데 찾으려 할때)

- IndexError(인덱스의 범위를 벗어 난 것)

- KeyError(딕셔너리에서 키가 없는 경우 발생)

- ModuleNoaFoundError(모듈을 찾을 수 없는 경우)

- importError(모듈을 찾았는데 안에서 무언가 못찾았을 때)

- KeyboardInterrupt(계속 돌때 강제 종료 시켰을 때 발생)



### 예외 처리

#### 기본 및 복수 - try except

![image-20200217155407957](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200217155407957.png)

> try절을 실행시키는데 예외가 발생되지 않으면, except없이 실행 종료하지만 예외가 발생하면 ***남은 부분을 수행하지 않고,*** except가 실행

![image-20200217161333607](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200217161333607.png)

#### 에러문구 처리

![image-20200217161410730](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200217161410730.png)

> else도 사용가능해

![image-20200217161427817](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200217161427817.png)

> finally는 예외 발생 여부와 관계없이  try떠날 때 항상 실행



#### 예외 발생시키기

`raise`를 사용함

>`raise 원하는오류('오류에 쓸말')`



### assert

![image-20200217164121787](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200217164121787.png)

> 이건 ~일거야! 단언하는게 assert 
>
> ex) 이건 트루일꺼야 근데 아니라면 에러가 나올거야..!