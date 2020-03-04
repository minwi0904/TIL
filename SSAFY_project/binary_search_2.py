numbers = int(input())
for number in range(numbers):
    P, Pa, Pb = list(map(int, input().split()))

    end = P
    count_a = 0
    binary_p = 0
    start_p = 1
    while binary_p != Pa:
        binary_p = (start_p + end) // 2
        count_a += 1
        if binary_p == Pa:
            break
        elif binary_p > Pa:
            end = binary_p
        else:
            start_p = binary_p

    count_b = 0
    binary_p = 0
    start_p = 1
    end = P
    while binary_p != Pb:
        binary_p = (start_p + end) // 2
        count_b += 1
        if binary_p == Pb:
            break
        elif binary_p > Pb:
            end = binary_p
        else:
            start_p = binary_p

    if count_a < count_b:
        result = 'A'
    elif count_b > count_a:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(number+1, result))

