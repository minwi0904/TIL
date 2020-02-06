arr = [1, 2, 3]
N = len(arr)
cnt = 0  #count의 준말
for i in range(1<<N): # << *2의 효과가 있어! 따라서 1<<3dms 1 > 1000이 된다고 보면됨(2진법)
    sub = []
    SUM = 0
    for j in range(N):
        if i & (1<<j): # &는 and연산이라는 뜻
            sub.append(arr[j])
    print(sub)
    for x in range(len(sub)):
        SUM += sub[x]
    if SUM == 0: # 공집합도 합은 0
        cnt += 1
