def calc(a, b):
    plus = a + b
    minus = a - b
    multiple = a * b
    divi = a / b
    try:
        divi = a / b
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다.')

    return plus, minus, multiple, divi

print(calc(5, 0))