T = int(input())
for t in range(1, T + 1):
    n = input()
    arr = list(map(int, input().split()))

    maxV = arr[0]  # 초기값 설정
    for i in arr:
        if i > maxV:
            maxV = i

    minV = arr[0]
    for i in arr:
        if i < minV:
            minV = i

    print('#{0} {1}'.format(t, maxV - minV))