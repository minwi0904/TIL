dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    stack = []
    stack.append((x, y, cnt)) # 지나간 위치 넣어주기
    while stack: # 스택이 비어있지 않으면 돌아가기
        ax, ay, cnt_n = stack.pop(0) # 스택의 첫번째꺼 빼서 각각 새로 넣어주기
        for i in range(4): # 4방향 탐색
            nx = ax + dx[i] #새로운 x설정
            ny = ay + dy[i] # 새로운 y설정
            if 0 <= nx < N and 0 <= ny < N: #범위 안벗어나는 친구들만 들어오기
                if maze[nx][ny] == '0': # 0을 만나면
                    maze[nx][ny] = 9 # 간데 9로 체크해주기
                    stack.append((nx, ny, cnt_n + 1)) # 지나갔으니까(9) 스택에 넣어주기
                elif maze[nx][ny] == '3':
                    return cnt_n #미로가 끝나면 리턴(거쳐온 갯수만큼)
    return 0 # 만약에 다 돌았는데 3을 못만나면 길이 없는 것 0 반환

numbers = int(input())

for number in range(numbers):
    N = int(input())
    maze = [list(input()) for i in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2': #시작점 찾기!
                result =  bfs(i, j, 0) # 위치, 갯수

    print('#{} {}'.format(number+1, result))
