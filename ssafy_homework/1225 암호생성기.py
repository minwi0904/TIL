for i in range(10):
    number = int(input())
    Num = list(map(int, input().split()))

    code = True
    while code:
        for i in range(1, 6):
            if Num[0] - i > 0:
                change = Num[0] - i
                Num.remove(Num[0])
                Num.append(change)
            else:
                Num.pop(0)
                Num.append(0)
                code = False
                break

    print('#{} '.format(number), end = '')
    print(*Num)
