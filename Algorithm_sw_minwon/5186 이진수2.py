numbers = int(input())

for number in range(numbers):
    N = float(input())
    result = ''
    N_10 = N
    while True:
        if len(result) <= 12:
            if N_10 * 2 == 1:
                result += '1'
                break
            elif N_10 * 2 > 1:
                result += '1'
                N_10 = N_10 * 2 - 1
            else:
                result += '0'
                N_10 = N_10 * 2
        else:
            break
    if len(result) <= 12:
        print('#{} {}'.format(number+1, result))
    else:
        print('#{} {}'.format(number+1, 'overflow'))

