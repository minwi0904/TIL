numbers = int(input())

for number in range(numbers):
    N, M, L = map(int, input().split())
    nodeList = [list(map(int, input().split())) for m in range(M)]

    tree = [[idx, 0] for idx in range(N+1)]
    for m in range(M):
        tree[nodeList[m][0]][1] = nodeList[m][1]

    for i in reversed(tree):
        tree[i[0] // 2][1] += i[1]
    print('#{} {}'.format(number+1,tree[L][1]))