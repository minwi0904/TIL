numbers = int(input())

for number in range(numbers):
    str1 = input()
    str2 = input()
    Maxval = 0

    str_dict = {}
    for i in str1:
        str_dict[i] = 0

    for i in str2:
        if i in str_dict:
            str_dict[i] = str_dict[i] + 1


    for key, val in str_dict.items():
        if val > Maxval:
            Maxval = val

    print('#{} {}'.format(number+1, Maxval))