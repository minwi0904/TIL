def omok():
    ppan = [[0]*21]
    omok_p = [[0] + list(map(int, input().split())) + [0] for i in range(19)]
    omok_pan = ppan + omok_p + ppan

    # for i in omok_pan:
    #     print(i)

    dx = [1, 1, 1, 0] # 우상향, 우하향, 우향, 하향
    dy = [-1, 1, 0, 1]
    dx_r = [-1, -1, -1, 0]
    dy_r = [1, -1, 0, -1]

    for j in range(1, 20):
        for i in range(1, 20):

            dol = omok_pan[i][j]
            if dol != 0:

                for n in range(4):
                    count = 1
                    x = j
                    y = i

                    if 0 <= x + dx[n] < 21 and 0 <= y + dy[n] < 21:
                        omok = True
                        while omok:
                            if omok_pan[y + dy[n]][x + dx[n]] == omok_pan[i][j]:
                                x += dx[n]
                                y += dy[n]
                                count += 1
                                # print(count)
                                if count > 5:
                                    omok = False
                            else:
                                 omok = False

                    if count == 5:
                        # print(n)
                        # print(omok_pan[i + dy_r[n]][j + dx_r[n]])
                        if omok_pan[i + dy_r[n]][j + dx_r[n]] != dol:
                            print(dol)
                            print(i, j)
                            return

    else:
        return print(0)

omok()