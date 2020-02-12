numbers = int(input())

for number in range(numbers):
    A = input()
    B = input()

    for i in range(len(B)-len(A)+1):
        Bi = i
        turn = True
        while turn:
            for j in range(len(A)):
                if A[j] == B[Bi]:
                    Bi += 1
                    j += 1
                else:
                    turn = False
                    break
            else:
                turn = False
        if j == len(A):
            print('#{} 1'.format(number+1))
            break
    else:
        print('#{} 0'.format(number+1))

