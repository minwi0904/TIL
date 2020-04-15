from collections import deque

numbers = int(input())

for number in range(numbers):
    N, M, K = map(int, input().split())
    start = list(map(int, input().split()))
    result = deque()
    result.extend(start)

    index = 0
    while K: # !!!!TRUE이고, 유효한 K번을 수행할거야!!!
        if index + M < N: # M번째칸에 칸추가하기 전에 수열 길이 넘냐 확인
            index = index + M # 새로운 인덱스
            temp = result[index] + result[index-1] # 두개 더해야할것 미리 만들기
            result.insert(index, temp) # 이제 추가해주기!!
            N += 1 #수열길이는 한개씩 이제 늘어남
        elif index + M == N: #마지막 위치라면? 첫번째 위치랑 더하기
            index = index + M
            temp = result[index - 1] + result[0]
            result.append(temp) #뒤에 붙여주는거니까
            N += 1
        else: #길이가 넘어가면, 앞에서와서 세주기
            index = index + M - N # 한바퀴돈 인덱스!!
            temp = result[index] + result[index - 1]
            result.insert(index, temp)
            N += 1
        K -= 1

    print('#{} '.format(number + 1), end='')
    if len(result) < 10:
        while result:
            print(result.pop(), end=' ')
    else:
        for i in range(10):
            print(result.pop(), end=' ')
    print('')