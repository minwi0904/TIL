import math
numbers = int(input())

for number in range(numbers):
    N = int(input())
    backHome = [list(map(int, input().split()))for n in range(N)]

    stack = [0]*N
    room = [0]*201
    studentMin = [math.ceil((min(backHome[n][0], backHome[n][1]))/2) for n in range(N)]
    studentMax = [math.ceil((max(backHome[n][0], backHome[n][1]))/2) for n in range(N)]
    student = [backHome[n][0] for n in range(N)]

    for idx in range(N): # 전부 거쳐갈 때마다 숫자 주기, 마지막에 젤 큰수 찾기
        if stack[idx] == 0:
            for k in range(studentMin[idx], studentMax[idx] + 1):
                room[k] += 1
                stack[idx] = 1

    print('#{} {}'.format(number + 1, max(room)))