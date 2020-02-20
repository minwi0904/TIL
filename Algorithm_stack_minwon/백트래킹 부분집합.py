TF = [0]*2
def makingRoom(room, dipth, wantN, TF):
    TF[0] = 1
    TF[1] = 0
    return 2

def backtrack(room, dipth, wantN):
    global powerset
    if dipth == wantN:
        result = 0
        for jj in range(1, 11):
            if room[jj] == 1:
                result += powerset[jj-1]
        if result == 10:
            subset = []
            for i in range(1, 11):
                if room[i] == 1:
                    subset.append(powerset[i-1])
            print(subset)
    else:
        dipth += 1
        two = makingRoom(room, dipth, wantN, TF)
        for i in range(two):
            room[dipth] = TF[i]
            backtrack(room, dipth, wantN)

Maxroom = 11
room = [0]*Maxroom
powerset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack(room, 0, 10)