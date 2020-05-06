def minSum(i, j, sum): # 행, 열, 합
    global N, minResult
    if i == j == N-1:
        if sum < minResult:
            minResult = sum
            return
    else:
        if sum > minResult:
            return
        else:
            if 0 <= i+1 <= N-1 and 0 <= j <= N-1: # 행+1
                minSum(i+1, j, sum+N_N[i+1][j])
            if 0 <= i <= N-1 and 0 <= j+1 <= N-1: # 열+1
                minSum(i, j+1, sum+N_N[i][j+1])

numbers = int(input())

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for i in range(N)]

    minResult = 1000000000000000000000
    minSum(0, 0, N_N[0][0])
    print('#{} {}'.format(number+1, minResult))