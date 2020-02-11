numbers = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for i in range(N)]

    for y in range(N):
        for x in range(N):
            room = N_N[y][x]
            move = 1

            check = True
            x_x = x
            y_y = y
            while check:
                for i in range(4):
                    if 0 <= x_x + dx[i] < N and  0 <= y_y + dy[i] < N:
                        if i == 0 and room + 1 == N_N[y_y+1][x_x]:
                            move += 1
                            y_y += 1
                            break
                        elif i == 1 and room + 1 == N_N[y_y][x_x+1]:
                            move += 1
                            x_x += 1
                            break
                        elif i == 2 and room + 1 == N_N[y_y-1][x_x]:
                            move += 1
                            y_y -= 1
                            break
                        elif i == 3 and room + 1 == N_N[y_y][x_x-1]:
                            move += 1
                            x_x -= 1
                            break
                            # for문이 0~4까지 다 도는동안 다음 숫자가 없다는걸 판별해야하는데
                            # 지금은 i는 0일때 딱 한번만 확인하고 check를 False로 만들어버리니까
                            # move가 한번 이상 안넘어가는거 !
                else:
                    check = False

            print(move)
