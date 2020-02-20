numbers = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for number in range(numbers):
    N = int(input())
    N_N = [[1] + list(map(int, input()))+ [1] for i in range(N)]
    N_N = [[1]*(N+2)] + N_N + [[1]*(N+2)]

    stack = []
    for i in range(N+2):
        for j in range(N+2):
            if N_N[i][j] == 2:
                stack.append((i, j))
                break

    result = 0
    while stack:
        road = stack.pop()
        if N_N[road[0]][road[1]] == 3:
            result = 1
            break
        else:
            N_N[road[0]][road[1]] = 1

        for mode in range(4):
            if N_N[road[0] + dy[mode]][road[1] + dx[mode]] == 0 or N_N[road[0] + dy[mode]][road[1] + dx[mode]] == 3:
                stack.append((road[0] + dy[mode], road[1] + dx[mode]))

    print('#{} {}'.format(number+1, result))


