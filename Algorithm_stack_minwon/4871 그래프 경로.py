numbers = int(input())

for number in range(numbers):

    V, E = list(map(int, input().split()))
    SandG = [list(map(int, input().split())) for e in range(E)]
    Start, Goal = list(map(int, input().split()))

    visited = [[] for i in range(V+1)] # 모두 False(길이 연결된지 확인하기 위한 초기값)
    road_stack = [] # Stack

    for i in range(len(SandG)):
        visited[SandG[i][0]].append(SandG[i][1])


    road_stack.append(Start) # 출발점지정
    visited_result = []
    while road_stack: # 스택이 []일 때 까지 돈다

        current = road_stack.pop()

        for i in visited[current]:
            if not i in visited_result:
                road_stack.append(i)

        visited_result.append(current)
        if current == Goal:
            break

    result = 0
    if visited_result[-1] == Goal:
        result = 1

    print('#{} {}'.format(number + 1, result))

