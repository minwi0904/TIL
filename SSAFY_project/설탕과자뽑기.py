h, w = list(map(int, input().split()))
pan = [[0]*w for i in range(h)]

numbers = int(input())
for number in range(numbers):
    l, d, x, y = list(map(int, input().split()))

    for i in range(l):
        if d == 0:
            pan[x-1][y-1+i] = 1
        else:
            pan[x-1+i][y-1] = 1

for i in pan:
    result = ''
    for j in range(w):
        result += str(i[j]) + ' '
    print(result[:-1])


