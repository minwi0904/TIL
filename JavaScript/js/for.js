// 기본 for문
for (let a = 0; a < 5 ; a++){
    console.log('hello')
}

let menus = ['짜장면', '짬뽕']

for (let menu of menus) {
    console.log(menu)
}

for (let menu in menus) {
    console.log(menu)
}

let numbers = {
    'gj': 062,
    'seoul': 02,
}

// key가 출력
for (let number in numbers) {
    console.log(number)
}

// 에러가 발생
for (let number of numbers) {
    console.log(number)
}