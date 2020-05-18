def find(array, num):
    left = 0
    right = N - 1
    flag = -1
    while True:
        m = (left + right)//2
        if num == array[m]:
            return 1
        else:
            if flag == -1:
                if num > array[m]:
                    flag = True
                    left = m + 1
                else:
                    flag = False
                    right = m -1
            else:
                if num > array[m]:
                    if flag:
                        return 0
                    else:
                        flag = True
                        left = m + 1
                else:
                    if flag:
                        flag = False
                        right = m - 1
                    else:
                        return 0




numbers = int(input())

for number in  range(numbers):
    N, M = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    list_a.sort()
    cnt = 0
    for i in range(M):
        if list_b[i] in list_a:
            cnt += find(list_a, list_b[i])
    print('#{} {}'.format(number + 1, cnt))