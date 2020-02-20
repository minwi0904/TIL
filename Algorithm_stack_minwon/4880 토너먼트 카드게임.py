def tournament(game):
    if len(game) == 1:
        return game

    a = tournament(game[:(len(game)+1)//2])
    b = tournament(game[(len(game)+1)//2:])

    # 가위 1, 바위 2, 보 3
    if a[0][1] == b[0][1]:
        return a
    elif abs(a[0][1] - b[0][1]) == 1 and a[0][1] < b[0][1]:
        return b
    elif abs(a[0][1] - b[0][1]) == 1 and a[0][1] > b[0][1]:
        return a
    elif abs(a[0][1] - b[0][1]) == 2 and a[0][1] < b[0][1]:
        return a
    else:
        return b

numbers = int(input())
for number in range(numbers):
    N = int(input())
    ggame = list(map(int, input().split()))
    game = []
    for idx, i in enumerate(ggame, 1):
        a = (idx, i)
        game.append(a)

    print('#{} {}'.format(number+1, tournament(game)[0][0]))

