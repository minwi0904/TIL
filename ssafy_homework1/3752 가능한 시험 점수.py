numbers = int(input())
# 문제니까 틀리고 맞고 밖에 없어
# 틀리거나 맞으면 최대점수일때 점수가 가장 큰 경우의 점수
# 즉 경우의 수는 그 점수 보다 작을 수 밖에 없어

for number in range(numbers):
    N = int(input())
    score = list(map(int, input().split()))

    scoreVisited = [0] * (sum(score) + 1) # 받을 수 있는 최대 점수로 리스트 만들기
    scoreVisited[0] = 1

    scoreTemp = 0
    for i in range(N):
        scoreTemp += score[i]
        for j in range(scoreTemp, -1, -1):
            if scoreVisited[j] == 1:
                scoreVisited[j + score[i]] = 1

    result = scoreVisited.count(1)
    print('#{} {}'.format(number+1, result))