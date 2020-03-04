numbers = int(input())

for number in range(numbers):
    N = int(input())
    ABi = []
    for i in range(N):
        Ai, Bi = map(int, input().split())
        ABi.append([Ai, Bi])

    P = int(input())
    Cj = []
    for j in range(P):
        Cj.append(int(input()))

    bus_stop = [0]*5001
    for n in range(len(ABi)):
        for idx, i in enumerate(range(ABi[n][1]-ABi[n][0]+1), ABi[n][0]):
            if idx in Cj:
                bus_stop[idx] += 1

    result = []
    for p in range(P):
        result.append(bus_stop[Cj[p]])

    print('#{} '.format(number+1), end ='')
    print(*result)
