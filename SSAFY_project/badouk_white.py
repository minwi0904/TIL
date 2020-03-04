numbers = int(input())

badouk_pan = [[0]*19 for i in range(19)]


for number in range(1, numbers+1):
    x, y = list(map(int, input().split()))
    badouk_pan[x-1][y-1] = 1


for badouk in badouk_pan:
    result = ''
    for i in range(19):
        result += str(badouk[i]) + ' '
    print(result[:-1])