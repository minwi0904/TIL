numbers = int(input())
for number in range(numbers):
    N, M = list(map(int, input().split()))
    game_pan = [[0]*N for i in range(N)]

    game_pan[(N-1)//2][(N-1)//2] = 2
    game_pan[(N-1)//2][round((N-1)/2)] = 1
    game_pan[round((N-1)/2)][(N-1)//2] = 1
    game_pan[round((N-1)/2)][round((N-1)/2)] = 2

    for i in game_pan:
        print(i)

    game_order = []
    for m in range(M):
        game_order.append(list(map(int, input().split())))

    for i in game_order:
        if i[2] == 1:
            game_pan[i[0]-1][i[1]-1] = 1
            if game_pan[][]


