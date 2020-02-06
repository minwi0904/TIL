numbers = int(input())
for number in range(numbers):
    dec = input()
    dec_list = []
    plus_dec = [13, 13, 13, 13]
    result = ''

    for i in range(0,len(dec),3):
        dec_list.append(dec[i:i+3])

    dec_set = set()
    for i in range(len(dec_list)):
        dec_set.add(dec_list[i])

    if len(dec_set) != len(dec)/3:
            result = ' ERROR'

    else:
        for i in range(len(dec_list)):
            if dec_list[i][0] == 'S':
                plus_dec[0] -= 1
            elif dec_list[i][0] == 'D':
                plus_dec[1] -= 1
            elif dec_list[i][0] == 'H':
                plus_dec[2] -= 1
            else:
                plus_dec[3] -= 1
        for i in range(len(plus_dec)):
            result += ' ' + str(plus_dec[i])

    print('#{}{}'.format(number+1, result))
