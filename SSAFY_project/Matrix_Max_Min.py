numbers = int(input())
for number in range(numbers):
    N, M = list(map(int, input().split()))
    N_N = [list(map(int, input().split())) for n in range(N)]

    M_M = []
    MaxNum = 0
    MinNum = 10000
    for i_N in range(N-M+1):
        M_M_m = []
        for j_N in range(N-M+1):
            result = 0
            for i_M in range(M):
                for j_M in range(M):
                    m_m = N_N[i_N + i_M][j_N + j_M]
                    result += m_m
            M_M_m.append(result)
            if result > MaxNum:
                MaxNum = result
            if result < MinNum:
                MinNum = result
        M_M.append(M_M_m)
    print('#{} {}'.format(number+1, M_M)+ '\n' + '최대 값 : {}, 최소 값 : {}'.format(MaxNum, MinNum))
