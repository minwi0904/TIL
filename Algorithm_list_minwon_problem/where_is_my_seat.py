numbers = int(input())
for number in range(numbers):
    N, K = list(map(int, input().split()))

    game_pan = []
    for n in range(N):
        list_game = list(map(int, input().split()))
        game_pan.append(list_game)
    # game_pan.append((N+1)*[0])

    seat_i = 0
    seat_j = 0
    # cnt_temp=[0]
    for i in range(N):#행 탐색
        count = 0
        n=0
        while n<N:
            if game_pan[i][n]==1:
                count+=1
                n+=1
            else:
                if count==K:
                    seat_i+=1
                count=0
                n+=1
        if count==K:
            seat_i+=1
    for j in range(N):#행 탐색
        count = 0
        n=0
        while n<N:
            if game_pan[n][j]==1:
                count+=1
                n+=1
            else:
                if count==K:
                    seat_j+=1
                count=0
                n+=1
        if count == K:
            seat_j += 1

    # seat_i = 0
    # seat_j = 0
    # for i in range(N+1):  # 행 탐색
    #     count = 0
    #     for j in range(N+1):  # 열 탐색
    #         count = 0
    #         if game_pan[i][j] == 1:
    #             n = j
    #             while game_pan[i][n] == 1:  # and n < N-j:
    #                 n += 1
    #                 count += 1
    #             if count == K:
    #                 seat_i += 1
    #         if count > K:
    #             break
    #
    # for i in range(N+1):#열 탐색
    #     count = 0
    #     for j in range(N+1):#행 탐색
    #         count = 0
    #         if game_pan[j][i] == 1:
    #             n = j
    #             while game_pan[n][i] == 1:
    #                 n += 1
    #                 count += 1
    #             if count == K:
    #                 seat_j += 1
    #         if count > K:
    #             break

    print(seat_i, seat_j)