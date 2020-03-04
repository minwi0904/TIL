numbers = int(input())

for number in range(numbers):
    n = int(input())
    color_pan = [[0] * 10 for i in range(10)]

    for i in range(n):
        y1, x1, y2, x2, c = list(map(int, input().split()))

        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                color_pan[i][j] += 1

        result =0
        for pan_n in color_pan:
            result += pan_n.count(2)

    print('#{} {}'.format(number+1, result))


