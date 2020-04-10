numbers = int(input())

for number in range(numbers):
    N, M, L = map(int, input().split())
    array = list(map(int, input().split()))
    for m in range(M):
        index, plus = map(int, input().split())
        array.insert(index, plus)
    print('#{} {}'.format(number+1, array[L]))
