def minCost(cnt, total): # 행, 비용
    global minResult
    if total > minResult: # 처음엔 끝까지 다 갔다가 그걸 기준으로 이제 돌리는 것!
        return
    if cnt == N - 1:
        if minResult > total:
            minResult = total
            return
    if cnt + 1 < N:
        for i in range(N):
            if visited[i] == -1: # 내가 간 열에는 다시 못찾아감! 안간 열에만 가야함.
                visited[i] = 1 # 갔다고 표시해놓고
                minCost(cnt + 1, total + plantCost[cnt+1][i]) # 들어갔다가 리턴 먹으면
                visited[i] = -1 # 안갔다고 표시하기


numbers = int(input())

for number in range(numbers):
    N = int(input())
    plantCost = [list(map(int, input().split())) for i in range(N)]

    minResult = 1000000000000000000000
    for i in range(N):
        visited = [-1]*N
        visited[i] = 1
        minCost(0, plantCost[0][i]) # 각각의 열에서 시작해서 탐색
    print('#{} {}'.format(number+1, minResult))