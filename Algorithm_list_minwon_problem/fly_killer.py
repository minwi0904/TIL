numbers = int(input())
for number in range(numbers):
    N, M = list(map(int, input().split()))
    floor = []
    for i in range(N):
        floor.append(list(map(int, input().split())))



    sum_fly_area_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_area = []
            for area_x in range(i, i+M):
                for area_y in range(j, j+M):
                    fly_area.append(floor[area_x][area_y])

            sum_fly_area = sum(fly_area)
            sum_fly_area_list.append(sum_fly_area)

    max_fly_area = max(sum_fly_area_list)

    print('#{} {}'.format(number+1, max_fly_area))
