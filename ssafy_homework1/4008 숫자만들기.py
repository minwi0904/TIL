def calc(num, Plus, Minus, Multiple, Divide, k):
    global maxNum
    global minNum
    if k == N: # 결론(내가 하고 싶은 종점!)
        if maxNum < num:
            maxNum = num
        if minNum > num:
            minNum = num
        return # 내가 원하는거 하고 끝내기

    nextNum = Nnum[k] # 계산은 혼자하는 게 아님, 다음 숫자를 지정해주기
    if Plus > 0:
        calc(num + nextNum, Plus-1, Minus, Multiple, Divide, k+1)
    if Minus > 0:
        calc(num - nextNum, Plus, Minus-1, Multiple, Divide, k+1)
    if Multiple > 0:
        calc(num * nextNum, Plus, Minus, Multiple-1, Divide, k+1)
    if Divide > 0:
        calc(int(num / nextNum), Plus, Minus, Multiple, Divide-1, k+1)

numbers = int(input())

for number in range(numbers):
    N = int(input())
    plus, minus, multiple, divide = list(map(int, input().split()))
    Nnum = list(map(int, input().split()))

    maxNum = -100000000
    minNum = 100000000
    first = Nnum[0] # 초기값 설정>> 이걸로 시작하고 연산자 만나면 하나씩 값 계산 되게
    calc(first, plus, minus, multiple, divide, 1)
    print('#{} {}'.format(number+1, maxNum-minNum))