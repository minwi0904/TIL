for number in range(1, 11):
    N = int(input())

    magneticPan = [list(map(int, input().split())) for n in range(N)]

    # 1은 N극 성질을 가지는 빨간색 자성체(S극인 아래쪽으로 향함)
    # 2는 S극 성질을 가지는 파란색 자성체(N극인 위쪽으로 향함)

    count = 0
    for i in range(N):
        isred = False
        for j in range(N):
            if magneticPan[j][i] == 1:
                isred = True
            elif magneticPan[j][i] == 2 and isred == True:
                count += 1
                isred = False
    print('#{} {}'.format(number,count))
