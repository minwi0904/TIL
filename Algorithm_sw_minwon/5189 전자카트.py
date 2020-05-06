from itertools import permutations

def factorial(n):
    global result
    if n == 1:
        return result
    else:
        return n * factorial(n-1)

def minBattery(state, count, roadN, battery): # 출발, 현재 횟수, 순열리스트,용량
    global minResult
    if count == N:
        if battery < minResult:
            minResult = battery
            return
    else:
        if battery > minResult:
            return
        else:
            if count< N-1:
                minBattery(roadN[count], count+1, roadN, battery + N_N[state - 1][roadN[count] - 1])
            else:
                minBattery(1, count + 1, roadN, battery + N_N[state - 1][0])

numbers = int(input())

for number in range(numbers):
    N = int(input())
    N_N = [list(map(int, input().split())) for i in range(N)]

    road = [i for i in range(2, N+1)]
    road_list = list(permutations(road, N-1))
    result = 1
    minResult = 1000000000000
    for n in range(factorial(N-1)):
        for m in range(2, N+1):
            minBattery(1, 0, road_list[n], 0)

    print('#{} {}'.format(number+1, minResult))