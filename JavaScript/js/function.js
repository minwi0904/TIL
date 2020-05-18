// def hello():
//     print('hello')

//함수 선언식
// function hello() {
//     console.log('hello')
// }
// hello()

//함수 표현식
const world = function () {
    console.log('world')
}
world()

// 화살표함수, function이라는 이름이 사라지고 =>로 빠르게 표현
const js = () => {
    console.log('js')
}
js()

const python = a => console.log(a)
python('hello python')

// 변수에 저장가능
// 함수에 리턴값으로 사용
// 함수의 인자로 사용

let numbers = [1, 2, 3, 4, 5]

// for (let number of numbers) {
//     console.log(number*2)
// }

const hello = () => {
    console.log('hello js')
}
hello()

numbers.forEach(num =>console.log(num*2))

