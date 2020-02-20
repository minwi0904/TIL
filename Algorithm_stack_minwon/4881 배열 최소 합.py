def permutation(count,total): # count =몇 번째 인가, total = 내가 탐색한 곳의 덧셈들
    global resultMin

    if count == N:
        if resultMin > total:
            resultMin = total
        return # 딱 원하는 값 찾고 함수 끝내기

    if total > resultMin: # N까지 아직 안왔을 때 total이 넘어버리면 cutting
        return # 함수 끝내기

    for column in range(N): # 0 ~ N-1까지
        if check[column] == 0:
            check[column] = 1
            permutation(count + 1, total + N_N[count][column])

            check[column] = 0 # 함수 끝났으면 다른데도 탐색하러 가야지

numbers = int(input())

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for i in range(N)]

    check = [0] * N
    resultMin = 10000000000
    permutation(0,0)

    print('#{} {}'.format(number+1, resultMin))