numbers = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for i in range(N)]

    Maxroom = [0,0]
    rooms = []
    room_dict = {}
    for y in range(N):
        for x in range(N):
            move = 1

            check = True
            x_x = x
            y_y = y
            while check:
                room = N_N[y_y][x_x]
                for i in range(4):
                    if 0 <= x_x + dx[i] < N and  0 <= y_y + dy[i] < N:
                        if room + 1 == N_N[y_y+dy[i]][x_x+dx[i]]:
                            move += 1
                            x_x += dx[i]
                            y_y += dy[i]
                            break
                            # for문이 0~4까지 다 도는동안 다음 숫자가 없다는걸 판별해야하는데
                            # 지금은 i는 0일때 딱 한번만 확인하고 check를 False로 만들어버리니까
                            # move가 한번 이상 안넘어가는거 !
                else:
                    check = False

            # room_dict[N_N[y][x]] = move # 딕트 개짱
            if move > Maxroom[0]:
                Maxroom = [move,N_N[y][x]]
            if move == Maxroom[0] and N_N[y][x] < Maxroom[1]:
                Maxroom = [move,N_N[y][x]]

            # Maxroom_num = 0
            # for key, val in room_dict.items():
            #     if val == Maxroom:
            #         if Maxroom
            #         Maxroom_num = key
            #         break


    print('#{} {} {}'.format(number+1, Maxroom[1], Maxroom[0]))