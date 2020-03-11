numbers = int(input())

for number in range(numbers):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    vote = [0]*len(Ai)
    for i in range(M):
        priceMax = Bi[i]
        n = 0
        out = True
        while out:
            if Ai[n] > priceMax:
                n += 1
            else:
                vote[n] += 1
                out = False

    maxIndex = 0
    maxScore = 0
    for idx, i in enumerate(vote, 1):
        if maxScore < i:
            maxScore = i
            maxIndex = idx

    print('#{} {}'.format(number+1, maxIndex))