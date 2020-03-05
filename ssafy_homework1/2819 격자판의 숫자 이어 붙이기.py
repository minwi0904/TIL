def numLen(n, i, j, numList): # n은 깊이, numList는 지금 숫자

    if n == 7:
        numLists.add(numList)
        return

    else:
        if 0<= i + dx[0] <4 and 0<= j + dy[0] < 4:
            ii, jj = i + dx[0], j + dy[0]
            numLen(n + 1, ii, jj, numList + fourSq[ii][jj])

        if 0<= i + dx[1] <4 and 0<= j + dy[1] < 4:
            ii, jj = i + dx[1], j + dy[1]
            numLen(n + 1, ii, jj, numList + fourSq[ii][jj])

        if 0<= i + dx[2] <4 and 0<= j + dy[2] < 4:
            ii, jj = i + dx[2], j + dy[2]
            numLen(n + 1, ii, jj, numList + fourSq[ii][jj])

        if 0<= i + dx[3] <4 and 0<= j + dy[3] < 4:
            ii, jj = i + dx[3], j + dy[3]
            numLen(n + 1, ii, jj, numList + fourSq[ii][jj])

numbers = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for number in range(numbers):
    fourSq = [list(map(str, input().split())) for i in range(4)]
    numLists = set()

    for i in range(4):
        for j in range(4):
            numLen(0, i, j, '')

    print('#{} {}'.format(number+1, len(numLists)))