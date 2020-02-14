numbers = int(input())

for number in range(numbers):
    n = int(input())

    Fn = [1, 3]

    for i in range(n//10 - 2):
        Fn.append(2 * Fn[i] + Fn[i + 1])

    print('#{} {}'.format(number+1, Fn[-1]))