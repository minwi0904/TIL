numbers = int(input())
for number in range(numbers):
    MaxResult = 0
    N, M = list(map(int, input().split()))
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if len(Ai) > len(Bj): # Ai가 짧은것, Bj가 긴것
        Ai, Bj = Bj, Ai

    for i in range(len(Bj) - len(Ai)+1):
        Ai_0 = len(Bj) * [0]
        Ai_0[i:i+len(Ai)] = Ai[::]

        result = 0
        for i in range(len(Bj)):
            result += (Ai_0[i] * Bj[i])

        if result > MaxResult:
            MaxResult = result

    print('#{} {}'.format(number+1, MaxResult))

