numbers = int(input())
for number in range(numbers):
    screw_n = int(input())
    screw_list = list(map(int, input().split()))

    odd_screw = []
    for i in range(len(screw_list)):
        if screw_list.count(screw_list[i]) % 2 == 1:
            odd_screw.append(screw_list[i])

    pair_screw = []
    for i in range(0, len(screw_list), 2):
        pair_screw.append([screw_list[i], screw_list[i+1]])

    for odd in odd_screw:
        odd_screw_index = screw_list.index(odd)
        for i in range(len(pair_screw)):
            if screw_list[odd_screw_index + 1] == pair_screw[i][0]:

