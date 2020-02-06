

T = int(input())
for i in range(1, T + 1):
    n = input()
    arr = list(map(int, input().split()))

maxV = val[0]  # 초기값 설정
for i in arr:
    if val[i] > maxV:
        maxV = val[i]

minV = val[0]
for i in arr:
    if val[i] < minV:
        minV = val[i]

print(f'#{T} {maxV - minV}')