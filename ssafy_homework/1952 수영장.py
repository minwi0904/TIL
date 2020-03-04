def perm(month, cost):
    if month >= 13: # 10월 11월에서도 3개월 요금이 가능함
        result_list.append(cost) # 모든 경우 계산된 결과값
        return
    if plan[month] == 0: # 달에 한번도 안가면 다음달로 바로 재귀 들어가기
        perm(month + 1, cost)
    else:
        perm(month + 1, cost + plan[month]*price[0])
        perm(month + 1, cost + price[1])
        perm(month + 3, cost + price[2])

numbers = int(input())

for number in range(numbers):
    price = list(map(int, input().split())) # 1일, 1달, 3달, 12달
    plan = [0] + list(map(int, input().split()))
    result_list = []

    perm(1, 0) # 1월 시작, 0원 계산
    result_list.append(price[3]) # 마지막 년간 가격
    print('#{} {}'.format(number+1, min(result_list)))
