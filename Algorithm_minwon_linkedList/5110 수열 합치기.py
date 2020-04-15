from collections import deque

numbers = int(input())

for number in range(numbers):
    N, M = map(int, input().split())
    arrays = [list(map(int, input().split())) for i in range(M)]

    result = deque() # result를 deque로 설정해서 최종적인 수열을 여기에 넣을거다.
    result.extend(arrays[0][:]) # 그리고 시작점을 설정한다. 첫번째 수열은 딱 다 들어가기!! insers는 인덱스를 써야함

    searchArray = 1 # Array마다 탐색
    Flag = False

    while searchArray < M: # 갯수(번째)보다 작은거면 들어가기
        for i in range(searchArray * N): # 수열 번째 * 각 수열 길이 = 총(하나) 수열 길이
            if result[i] > arrays[searchArray][0]: # 탐색시작, 만약 총수열 i번째 숫자가 다음 수열(searchArray번째)의 첫번째 숫자보다 작으면
                Flag = True # 찾았당
                index = i # index는 i이다
                break #for문을 빠져 나가자(index찾기끝났으니 다른 작업아래에서 하자.)

        if Flag: #Flag가 True면
            for i in range(N-1, -1, -1): # 인덱스 역순으로
                result.insert(index, arrays[searchArray][i]) #insert는 하나만 넣을 수 있어
                # 그니까, 같은자리에 계속 넣으려면 뒤부터 넣어야지 정방향으로 전부 들어감
            searchArray += 1 # 지금 어레이에서 할일 끝났으니까 다음 어레이로 넘어가기
            Flag = False #이것도 다시쓰려면 초기화 해주기
        else: # 위에서 전부 돌았는데 플레그가 안바뀌면! 뒤에 붙여주기
            result.extend(arrays[searchArray][:])
            searchArray += 1

    print('#{} '.format(number+1), end='')
    for i in range(10):
        print(result.pop(), end=' ')
    print('')
