def bfs(start, end):
    visited[start] = 1 # 스타트 방문 완료
    stack = []
    stack.append((start, 0)) # 이것도 몇번 거치는지 알아야해 간선 갯수=count 필요함

    while stack: # 스택이 비지 않으면 동작
        x, cnt = stack.pop(0) # 스택0번째 원소 빼기
        for i in graph[x]: # 스택에서 뺀 노드에 연결된 다른 노드들 만큼 돌려라(다음에 내가 갈곳을 찾는 친구)
            if i == end: # 포문 돌리다가 노드에 연결된 친구가 end!일때!!!!!!
                return cnt+1 # 기존 움직임+1해서 함수 끝내기
            elif visited[i] == 0: # 돌고 있는데 방문안한 새로운 곳이면?
                stack.append((i, cnt+1))# 스택에 넣어주기(다음에 방문할거라서)
                visited[i] = 1 # 그리고 현재 내가 있는 노드는 방문했다고 하기
    return 0 # 전부 돌았는데 end로 못갔으면 0반환

numbers = int(input())

for number in range(numbers):
    V, E = map(int, input().split()) #V는 노드 갯수, E는 간선 갯수
    graph = [[] for i in range(V+1)] # 노드 방

    for i in range(E):  # 간선 만큼 돌려주기
        x, y = map(int, input().split()) # 간선들 인풋 넣어주기
        graph[x].append(y) # 그래프에 노드x번이 y번으로 연결된걸 알려주는것
        graph[y].append(x) # 양방향이니까 노드 y번이 x번으로도 갈 수 있는거 알려주는 것

    S, G = map(int, input().split()) # S는 스타트, G는 골
    visited = [0]*(V+1) # 노드갯수만큼 노드거쳤나 안거쳤나 확인하기
    result = bfs(S, G) # 드디어 함수 등장..! 시작과 끝!
    print('#{} {}'.format(number+1, result))
