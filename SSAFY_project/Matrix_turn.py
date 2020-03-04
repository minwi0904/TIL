numbers = int(input())
for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for n in range(N)]
    N_N_90 = [[0] * N for n in range(N)]
    N_N_180 = [[0] * N for n in range(N)]
    N_N_270 = [[0] * N for n in range(N)]
    N_N_result = [['']*3 for n in range(N)]

    for i in range(N):
        for j in range(N):
            N_N_90[i][N - j - 1] = N_N[j][i]

    for i in range(N):
        for j in range(N):
            N_N_180[i][N - j - 1] = N_N_90[j][i]

    for i in range(N):
        for j in range(N):
            N_N_270[i][N - j - 1] = N_N_180[j][i]

    for index, str_i in enumerate(N_N_90):
        str_result = ''
        for j in range(N):
            str_result += str(str_i[j])
        N_N_result[index][0] = str_result

    for index, str_i in enumerate(N_N_180):
        str_result = ''
        for j in range(N):
            str_result += str(str_i[j])
        N_N_result[index][1] = str_result

    for index, str_i in enumerate(N_N_270):
        str_result = ''
        for j in range(N):
            str_result += str(str_i[j])
        N_N_result[index][2] = str_result

    print('#{}'.format(number+1))
    for n in N_N_result:
        result = ''
        for idx in range(3):
            result += n[idx] + ' '
        print(result[:-1])