numbers = int(input())

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, list(input()))) for i in range(N)]


    if N == 1:
        start = 0
        end = 0
        result = N_N[0][0]
    else:
        start = N_N[0][N//2]
        end = N_N[N-1][N//2]
        result = 0
        for i in range(1, N - 1):

            if i > N // 2:
                result += sum(N_N[i][N // 2 - N + i + 1 :N // 2 + N - i])
            else:
                result += sum(N_N[i][N // 2 - i: N // 2 + i + 1])


    print('#{} {}'.format(number+ 1, start + result + end))
