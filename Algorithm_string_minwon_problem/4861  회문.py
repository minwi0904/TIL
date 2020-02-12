numbers = int(input())

for number in range(numbers):
    result = ''
    N, M = list(map(int, input().split()))
    N_N = [input() for i in range(N)]



    for x in range(N):
        for y in range(N - M + 1):
            result_y = ''
            count_y = 0
            for m in range(M // 2):
                if N_N[y + m][x] == N_N[y + M-1 - m][x]:
                    count_y += 1
                    if count_y == M // 2:

                        for mm in range(M):
                            result_y += N_N[y + mm][x]
                        else:
                            break
                else:
                    break

            if len(result_y) == M:
                result = result_y
                break


    for y in range(N):
        for x in range(N - M + 1):
            result_x = ''
            count_x = 0
            for m in range(M // 2):
                if N_N[y][x + m] == N_N[y][x + M-1 - m]:
                    count_x += 1
                    if count_x == M // 2:
                        for mm in range(M):
                            result_x += N_N[y][x + mm]
                        else:
                            break
                else:
                    break
            if len(result_x) == M:
                result = result_x
                break

    print('#{} {}'.format(number+1, result))


