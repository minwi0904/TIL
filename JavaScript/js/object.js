const me = {
    name: 'change',
    location: 'gj',
    language: ['python', 'js', 'sql'],
    products: {
        phone: 'iphone',
        computer: 'desktop',
    },
    greeting: function(){return 'hihi'},
    // 여러분들의 나이를 받아서 2배 시켜봅시다.
    double: (age) => {console.log(age*2)}

}
// js()

// () => {console.log('python')}
// console.log(me.double(100))

console.log(me)

// json
let meJson = JSON.stringify(me)
console.log(meJson)

// json
let meObject = JSON.parse(meJson)
console.log(meObject)