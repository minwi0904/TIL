numbers = int(input())
for number in range(numbers):
    P, Pa, Pb = list(map(int, input().split()))


    count_a = 0
    binary_P = 0
    start_P = 0

    while binary_P != Pa:
        binary_P = (start_P + P) // 2
        if binary_P > Pa:
            P = binary_P
        else:
            start_P = binary_P
        count_a += 1

    count_b = 0
    binary_P = 0
    start_P = 0

    while binary_P != Pb:
        binary_P = (start_P + P) // 2
        if binary_P > Pb:
            P = binary_P
        else:
            start_P = binary_P
        count_b += 1

    print(count_a, count_b)