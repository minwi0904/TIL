def combination(n, r):
    result_son = 1
    result_mom = 1
    for i in range(r):
        result_son *= (n - i)
        result_mom *= (r - i)
    return result_son // result_mom
# print(combination(0, 0))

numbers = int(input())
for number in range(numbers):
    dan_pascal = int(input())

    pascal_list = []
    for dan in range(dan_pascal):
        for i in range(dan+1):
            result = combination(dan, i)
            pascal_list.append(result)

    print('#{}'.format(number + 1))

    idx = 0
    for i in range(dan_pascal):
        pascal_picture = ''
        for j in range(i+1):
            pascal_picture += str(pascal_list[idx]) + ' '
            idx += 1
        print(pascal_picture[:-1])

