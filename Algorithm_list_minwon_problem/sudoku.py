# import sys
# sys.stdin = open("input.txt", "r")

numbers = int(input())

for n in range(numbers):
    sudoku_n = [list(map(int,input().split())) for i in range(9)]

    result = 1
    for i in range(9):
        for j in range(9):
            verification_horizontal = set()
            verification_vertical = set()
            verification_horizontal.add(sudoku_n[i][j])
            verification_vertical.add(sudoku_n[j][i])

        if len(verification_horizontal) != 9:
            result = 0
            print("야")
            break
        if len(verification_vertical) != 9:
            result = 0
            print("호")
            break

    trg = 0
    for nine_i in range(0,9,3):
        for nine_j in range(0,9,3):
            verification_rectangle = set()
            for i in range(3):
                for j in range(3):
                    verification_rectangle.add(sudoku_n[nine_i+i][nine_j+j])
                if len(verification_rectangle) != 9:
                    trg = 1
                    result = 0
                    break
            if trg:
                break
        if trg:
            break

    print(result)





