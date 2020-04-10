from collections import deque

numbers = int(input())

for number in range(numbers):
    N, M, L = map(int, input().split())
    queue = deque() # depue만들어 주기 스택과 큐의 기능 한번에 갖기
    array = list(map(int, input().split()))

    queue.extend(array) #append와 다르게 이친구는 array전체를 리스트 끝에 전부 넣는다.
    for m in range(M):
        condition = list(input().split())
        if condition[0] == 'I': # I, D, S세가지 경우 존재
            queue.insert(int(condition[1]), condition[2])
        elif condition[0] == 'D':
            del queue[int(condition[1])]
        else:
            queue[int(condition[1])] = condition[2]
    if len(queue) > L:
        print('#{} {}'.format(number+1, queue[L]))
    else:
        print('#{} {}'.format(number + 1, -1))