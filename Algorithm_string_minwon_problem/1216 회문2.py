for i in range(10):
    number = int(input())
    N_N = [input() for i in range(100)]
    N_N_90 = [[0]*100 for i in range(100)]

    for i in range(100):
        for j in range(100):
            N_N_90[i][100 - 1 - j] = N_N[j][i]

    MaxNum = 0
    result2= ""
    for num in range(100, 0, -1): # 회문의 길이

        for i in range(100): # 가로탐색
            for j in range(100 - num + 1):

                for n in range(num // 2):
                    if N_N[i][j + n] == N_N[i][j + num - 1 - n]:
                        pass
                    else:
                        break
                else:
                    if bool(N_N[i][j:num]) == False:
                        pass
                    else:
                        if len(N_N[i][j:num]) > MaxNum:
                            MaxNum = len(N_N[i][j:num])
                            result2 = N_N[i][j:num]
    print('d', result2)
    # for num in range(100, 0, -1): # 회문의 길이
    #
    #     for i in range(100): # 가로탐색
    #         for j in range(100 - num + 1):
    #
    #             for n in range(num // 2):
    #                 if N_N_90[i][j + n] == N_N_90[i][j + num - 1 - n]:
    #                     pass
    #                 else:
    #                     break
    #             else:
    #                 if bool(N_N_90[i][j:num]) == False:
    #                     pass
    #                 else:
    #                     if len(N_N_90[i][j:num]) > MaxNum:
    #                         MaxNum = len(N_N_90[i][j:num])



    for num in range(100, 0, -1): # 회문의 길이

        for j in range(100): # 세로탐색
            for i in range(100 - num + 1):

                result = ''
                for n in range(num // 2):
                    if N_N[i + n][j] == N_N[i + num - 1 - n][j]:
                        pass
                    else:
                        break
                else:
                    for iii in range(num):
                        result += N_N[i+iii][j]
                    if bool(len(result)) == False:
                        pass
                    else:
                        print(MaxNum, result)
                        if len(result) > MaxNum:
                            MaxNum = len(result)
                            print(result)

    print('#{} {}'.format(number, MaxNum))



