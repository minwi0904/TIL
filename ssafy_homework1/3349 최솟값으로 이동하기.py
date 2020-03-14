def searchRoad(start, end): #n은 거친 횟수, i, j는 위치
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    if (dx >= 0 and dy >=0) or (dx < 0 and dy < 0): #우상향 위치에 존재할 때, 부호가 같을 때
        dx = abs(dx)
        dy = abs(dy)
        if dy > dx: # 두개 중 더 길이가 큰 길이만큼 이동해야하기 때문에
            dx, dy = dy, dx
        count[0] = count[0] + dx
        return
    else:
        count[0] = count[0] + abs(dx) + abs(dy) #부호가 다르다면, dx+dy크기만큼 이동해줘야함
        return

numbers= int(input())

for number in range(numbers):
    W, H, N = map(int, input().split())
    start = list(map(int, input().split()))

    count = [0] #리스트로 쓰면 전역변수 안해도됨
    for i in range(N-1):
        end = list(map(int, input().split()))
        searchRoad(start, end) # 원하는 위치로 가기 (i번째)
        start = end # 함수가 끝나면 다시 (i+1번째를 계산하기 위해서)
    print('#{} {}'.format(number+1, count[0]))






