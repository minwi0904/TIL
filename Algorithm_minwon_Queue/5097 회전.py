numbers = int(input())

for number in range(numbers):
    N, M = list(map(int, input().split()))
    Nlist = list(map(int, input().split()))
    m = M % N
    print('#{} {}'.format(number+1, Nlist[m]))