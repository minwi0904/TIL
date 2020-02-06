datas = list(map(int, input().split()))

counts = [0]*len(max(data)+1)

for i in range(len(datas)):
    datas[i] += 1