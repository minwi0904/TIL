ant_house = [list(map(int, input().split())) for i in range(10)]

if ant_house[1][1] == 0:
    ant_house[1][1] = 9
x = 1
y = 1
while True:
    if ant_house[y][x] == 2:
        ant_house[y][x] = 9
        break

    if ant_house[y][x + 1] == 0 or ant_house[y][x + 1] == 2:
        if ant_house[y][x + 1] == 2:
            ant_house[y][x + 1] = 9
            break
        ant_house[y][x + 1] = 9
        x = x + 1

    elif ant_house[y + 1][x] == 0 or ant_house[y + 1][x] == 2:
        if ant_house[y + 1][x] == 2:
            ant_house[y + 1][x] = 9
            break
        ant_house[y + 1][x] = 9
        y = y + 1

    else:
        break

for i in ant_house:
    result = ''
    for j in range(10):
        result += str(i[j]) + ' '
    print(result[:-1])