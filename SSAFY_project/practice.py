for i in range(1, 11):
    number = int(input())
    result_hundred = []
    for j in range(100):
        hundred_list = list(map(int, input().split()))
        result_hundred.append(hundred_list)

    row_sum_list = []
    for row in result_hundred:
        row_sum= sum(row)
        row_sum_list.append(row_sum)
    max_row = max(row_sum_list)

    column_sum_list = []
    for column in range(len(result_hundred[0])):
        column_sum = 0
        for row in range(len(result_hundred[0])):
             column_sum += result_hundred[row][column]
        column_sum_list.append(column_sum)
    max_column = max(column_sum_list)

    diagonal_sum1 = 0
    diagonal_sum2 = 0
    for i in range(len(result_hundred[0])):
        diagonal_sum1 += result_hundred[i][i]
        diagonal_sum2 += result_hundred[i][99-i]

    max_sum = max(max_row, max_column, diagonal_sum1, diagonal_sum1, diagonal_sum2 )
    print('#{} {}'.format(number, max_sum))
