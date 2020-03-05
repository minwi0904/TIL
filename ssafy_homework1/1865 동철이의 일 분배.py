def success(n, prob): # n, k은 단계(어디까지, 나는 어디에 있나), prob은 가능성
    global maxP
    if prob <= maxP: # prob는 작아지면 작아졌지 절대 커지지 않아 확률이니까!=도 꼭 넣어줘야함
        return
    if n == N: # 끝까지 다 돌았을 때 return
        if prob > maxP:
            maxP = prob
        return

    for i in range(N):
        if visited[i] == False:
            visited[i] = True # i 들릴거야 선포하고 i번째 들리기(아래 재귀)
            success(n + 1, prob * Pi[n][i] * 0.01) # 위에를 트루로 만들어주면 안간데만 들릴 수 있음
            visited[i] = False # i 갔다왔어, 그니까 이제 여기 말고 다른데 갈거야

numbers = int(input())
for number in range(numbers):
    N = int(input())
    Pi = [list(map(int, input().split())) for j in range(N)] # i는 사람

    maxP = 0
    visited = [False]*N
    success(0, 1)
    print('#{0} {1:0.6f}'.format(number+1, maxP*100))
