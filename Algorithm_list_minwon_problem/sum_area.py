numbers = int(input())
for number in range(1, numbers+1):
    N,M = map(int, input().split())
    number_areas = list(map(int, input().split()))
    result = []
    for i in range(N-2):
        sum3 = number_areas[i]+ number_areas[i+1] + number_areas[i+2]
        result.append(sum3)
    max_result = max(result)
    min_result = min(result)
    answer = max_result - min_result
    print('#{} {}'.format(number, answer))
