for number in range(10):
    number_ladder = int(input())
    ladder_picture = []
    for i in range(100):
        ladder_line = list(map(int, input().split()))
        ladder_picture.append(ladder_line)

    minNum = 1000
    idx = 0
    for i in range(100):
        if ladder_picture[0][i] == 1:
            start = i
            j = 0
            right = 0
            left = 0
            cnt = 0
            while j != 99:
                cnt += 1
                if start-1 >= 0 and ladder_picture[j][start-1] == 1 and right != 1:
                    start -= 1
                    left = 1
                    right = 0
                elif start+1 <= 99 and ladder_picture[j][start+1] == 1 and left != 1:
                    start += 1
                    right = 1
                    left = 0
                elif ladder_picture[j+1][start] == 1:
                    j += 1
                    right = 0
                    left = 0
                if cnt > minNum:
                    break
            if cnt < minNum:
                minNum = cnt
                idx = i
    print('#{} {}'. format(number+1, idx))
