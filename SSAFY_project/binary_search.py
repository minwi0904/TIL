numbers = int(input())
for number in range(numbers):
    P, Pa, Pb = list(map(int, input().split()))

    count_a = 0
    binary_P = 0
    start_P = 0
    while binary_P != Pa:
        binary_P = (start_P + P) // 2
        count_a += 1
        if binary_P > Pa:
            if abs(Pa - binary_P) > abs(Pa - start_P):
                P = binary_P // 2
                count_a += 1
            elif abs(Pa - binary_P) == Pa:
                count_a += 1
                break
            else:
                start_P = (start_P + binary_P) // 2
                count_a += 1
        elif binary_P == Pa:
            count_a += 1
            break
        else:
            if abs(Pa - start_P) > abs(Pa - binary_P):
                start_P = (start_P + binary_P) // 2
                P = binary_P
                count_a += 1
            elif abs(Pa - P) == abs(Pa - binary_P):
                count_a += 1
                break
            else:
                start_P = (P + binary_P) // 2
                count_a += 1

    count_b = 0
    binary_P = 0
    start_P = 0
    while binary_P != Pb:
        binary_P = (start_P + P) // 2
        count_b += 1
        if binary_P > Pb:
            if abs(Pb - binary_P) > abs(Pb - start_P):
                P = binary_P // 2
                count_b += 1
            elif abs(Pb - binary_P) == Pb:
                count_b += 1
                break
            else:
                start_P = (start_P + binary_P) // 2
                count_b += 1
        elif binary_P == Pa:
            count_b += 1
            break
        else:
            if abs(Pb - start_P) > abs(Pb - binary_P):
                start_P = (start_P + binary_P) // 2
                P = binary_P
                count_b += 1
            elif abs(Pb - P) == abs(Pb - binary_P):
                count_b += 1
                break
            else:
                start_P = (P + binary_P) // 2
                count_b += 1

    print(count_a, count_b)