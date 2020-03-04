numbers = int(input())
for number in range(numbers):
    color_box_numbers = int(input())

    box_list = []
    red_box = []
    blue_box = []
    for color_box_number in range(color_box_numbers):
        box_index = list(map(int, input().split()))
        box_list.append(box_index)
        if box_list[color_box_number][4] == 1:
            red_box.append(box_index)
        else:
            blue_box.append(box_index)

    red_box_list = []
    for i in range(len(red_box)):
        red_start = [red_box[i][0], red_box[i][1]]
        for x in range(red_box[i][2] - red_box[i][0]+1):
            for y in range(red_box[i][3]-red_box[i][1]+1):
                red_color = (red_start[0]+x, red_start[1]+y)
                red_box_list.append(red_color)
    red_box_area = list(set(red_box_list))


    blue_box_list =[]
    for i in range(len(blue_box)):
        blue_start = [blue_box[i][0], blue_box[i][1]]
        for x in range(blue_box[i][2]-blue_box[i][0]+1):
            for y in range(blue_box[i][3] - blue_box[i][1]+1):
                blue_color = (blue_start[0]+ x, blue_start[1]+y)
                blue_box_list.append(blue_color)

    count = 0
    for red_area in red_box_area:
        for blue_area in blue_box_list:
            if red_area == blue_area:
                count += 1

    print('#{} {}'.format(number+1, count))