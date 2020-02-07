numbers = int(input())
for number in range(numbers):
    string_list = []
    for string in range(5):
        string = input()
        string_list.append(string)

    len_string = 0
    for i in range(len(string_list)):
        if len(string_list[i]) > len_string :
            len_string = len(string_list[i])

    result = ''
    for i in range(len_string):
        for j in range(5):
            if i < len(string_list[j]):
                result += string_list[j][i]

    print('#{} {}'.format(number+1, result))

