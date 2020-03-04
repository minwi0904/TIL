pan = [list(map(int, input().split())) for i in range(19)]

cross_num = int(input())
for n in range(cross_num):
    x, y = list(map(int, input().split()))
    for j in range(19):
        if pan[x-1][j] == 1:
            pan[x-1][j] = 0
        else:
            pan[x-1][j] = 1

        if pan[j][y-1] == 1:
            pan[j][y-1] = 0
        else:
            pan[j][y-1] = 1

for p in pan:
    result = ''
    for i in range(19):
        result += str(p[i]) + ' '
    print(result[:-1])