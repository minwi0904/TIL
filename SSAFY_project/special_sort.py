numbers = int(input())
for number in range(numbers):
    len_number_list = int(input())
    number_list = list(map(int, input().split()))
    number_list.sort()

    special_list = []
    for i in range(5):
        special_list.append(number_list[len(number_list)-1-i])
        special_list.append(number_list[i])

    result = ''
    for j in special_list:
        result = result + ' ' + str(j)

    print('#{}{}'.format(number+1, result))
