numbers = int(input())

for number in range(numbers):
    s = input()

    j = 0
    S_stack = []

    for j in range(len(s)):
        if S_stack == []:
            S_stack.append(s[j])
        else:
            if s[j] != S_stack[-1]:
                S_stack.append(s[j])
            else:
                S_stack.pop()

    print('#{} {}'.format(number+1, len(S_stack)))
