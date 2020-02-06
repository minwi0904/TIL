numbers = int(input())
for number in range(numbers):
    N = int(input())
    number_list = list(map(int, input().split()))

    bigger_bigger = []
    # for idx, i in enumerate(number_list):
    for i in range(len(number_list)-1):
        for j in number_list[i+1:]:
            ij = str(number_list[i] * j)
            print(ij)
            for n in range(len(ij)-1):
                if int(ij[n]) > int(ij[n+1]):
                    break
            else:
                bigger_bigger.append(ij)

    if bigger_bigger == []:
        bigger_bigger.append(-1)

    bigger_bigger_int = list(map(int, bigger_bigger))
    max_bigger = max(bigger_bigger_int)

    print('#{} {}'.format(number+1, max_bigger))
