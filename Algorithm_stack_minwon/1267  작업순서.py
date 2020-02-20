for number in range(1, 11):

    V, E = list(map(int, input().split()))
    road_basic = list(map(int, input().split()))

    people = [i for i in range(1, V + 1)]
    dochak = [[] for i in range(V + 1)]
    dochakList = []

    for e in range(E):
        dochak[road_basic[2 * e]].append(road_basic[2 * e + 1])
    for e in range(E):
        dochakList.append(road_basic[2 * e + 1])

    stack = []  # helper 앞으로 갈 수 있는 곳, 미래
    for sijak in people:
        if sijak not in dochakList:
            stack.append(sijak)

    visitedList = []
    while stack:
        current = stack.pop()

        for neighbor in dochak[current]:
            if neighbor not in visitedList:
                dochakList.remove(neighbor)
                if neighbor not in dochakList:
                    stack.append(neighbor)

        visitedList.append(current)

    print('#{} '.format(number), end='')
    print(*visitedList)


