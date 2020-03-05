numbers = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for i in range(N)]

    room = []
    Maxroom = 0
    for i in range(N):
        for j in range(N):

            count = 1
            f_count = 0
            y, x = i, j
            check = True
            while check:
                f_count += 1
                for n in range(4):
                    if 0 <= y + dy[n] < N and 0 <= x + dx[n] < N:
                        if N_N[y + dy[n]][x + dx[n]] == N_N[y][x] + 1:
                             y = y + dy[n]
                             x = x + dx[n]
                             count += 1
                             break
                else:
                    if count == 0:
                        check = False
                    elif f_count == count:
                        check = False

            if count > 1:
                if count > Maxroom:
                    Maxroom = count
                    room = []
                    room.append([N_N[i][j], count])
                elif count == Maxroom:
                    room.append([N_N[i][j], count])


    room.sort()

    print('#{} '.format(number + 1), end='')
    print(*room[0])
