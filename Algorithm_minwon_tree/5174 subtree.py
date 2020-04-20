numbers = int(input())

for number in range(numbers):
    E, N = map(int, input().split())
    nodeList =  list(map(int, input().split()))
    parent = [[] for i in range(E+2)] # 간선+1이 노드갯순데 0은 무시할거야
    # visited = [0]*(E+2) #트리는 visited를안써도됨

    for i in range(1, 2*E+1, 2): # 정렬 해주기
        parent[nodeList[i-1]].append(nodeList[i])

    stack = []
    stack.append(N)

    count = 0
    while stack:
        temp = stack.pop()
        # visited[temp] = 1 #
        if parent[temp] != []:
            count += len(parent[temp])
            stack.extend(parent[temp])

    print('#{} {}'.format(number+1, count+1))