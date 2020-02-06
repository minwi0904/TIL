# arr = [x for x in input()]
# arr = [int(x) for x in input()]
# arr = list(input().split())
# arr = list(map(int, input().split()))

Arr = [int(x) for x in input()]

c =[0]*10

for i in range(len(Arr)):
    n = Arr[i]
    c[n] += 1

    # CNT[ARR[i]] += 1
i = 0
triple = 0
run = 0
while i < len(c):
    if c[i] >= 3:
        c[i] -= 3
        triple += 1
        continue
    if i < 8 and c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + triple == 2:
    print('Baby Gin')
else:
    print('Lose')
