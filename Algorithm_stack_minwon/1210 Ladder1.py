for i in range(10):

    number = int(input())
    ladder_pan = [[0] + list(map(int, input().split())) + [0] for i in range(100)]

    dx = [-1, 1, 0]

    ladder_start = []
    for i in range(1, 101):
        if ladder_pan[0][i] == 1:
            ladder_start.append(i)

    result = 0
    for i in ladder_start:
        y = i
        for j in range(99):

            if ladder_pan[j][y + 1] == 0 and ladder_pan[j][y - 1] == 0:
                ladder = False
            elif ladder_pan[j][y + 1] == 1:
                ladder = True
                mode = 1
            elif ladder_pan[j][y - 1] == 1:
                ladder = True
                mode = 0

            while ladder:
                if ladder_pan[j][y + dx[mode]] == 1:
                    y += dx[mode]
                else:
                    ladder = False

        else:
            if ladder_pan[99][y] == 2:
                result = i - 1
                break

    print('#{} {}'.format(number, result))
