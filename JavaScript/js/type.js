var c = 'asdf'
// let과 const는 둘다 중복생성 X
//
let a = 123
a = 456 // let은 재할당 가능
//
const b = 'hello'
// b = 'world' const(상수)는 재할당 불가.


console.log(typeof 123)
let name = 'change'
let hello_msg = `hello ${name}`
console.log(hello_msg)

// True, False
console.log(true)

console.log(undefined) //할당이 되지 않았다!

console.log(true && ture) //and
console.log(true || ture) //or

result = true ? 1 : 2
console.log(result) //참이면 앞, 틀리면 뒤 실행

