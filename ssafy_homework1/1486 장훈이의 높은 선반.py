import itertools
numbers = int(input())

for number in range(numbers):
    N, B = map(int, input().split())
    N_list = list(map(int, input().split()))

    gumsa = []
    minNum = 1000000000
    for n in range(1, N+1):
        com = itertools.combinations(N_list, n)

        for i in com:
            result = 0
            for j in i:
                result += j
            if result >= B:
                gumsa.append(result)

    for i in gumsa:
        if (i - B) < minNum:
            minNum = i - B

    print('#{} {}'.format(number+1, minNum))


