def calc(a, b):
    plus = a + b
    minus = a - b
    multiple = a * b
    try:
        division = a / b
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다.')

    return plus, minus, multiple, division

print(calc(5, 0))