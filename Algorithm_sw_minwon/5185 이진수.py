numbers = int(input())

for number in range(numbers):
    N, N_16 = input().split()
    result = ''
    for i in N_16:
        N_10 = int(i, 16) # 16진수를 10진수로 바꿔주는 것.(int에 두번째 인자가 들어가면)
        N_2 = format(N_10, 'b') # 10진수를 다른 수로 바꿔주기!! b는 2진수 o는 8진수x는 16진수
        if len(N_2) < 4:
            for i in range(4 - len(N_2)):
                result += '0'
        result += N_2
    print('#{} {}'.format(number+1, result))

