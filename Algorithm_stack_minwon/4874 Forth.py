numbers = int(input())

for number in range(numbers):
    calc = input().split()
    stack = []

    for token in calc:
        if token.isdigit() == True:
            stack.append(token)
        elif token == '.':
            pop_clac = stack.pop()
            if stack != []:
                pop_clac = 'error'
                break
        else:
            if len(stack) < 2:
                pop_clac = 'error'
                break
            else:
                pop2 = int(stack.pop())
                pop1 = int(stack.pop())
                if token == '+':
                    result = pop1 + pop2
                    stack.append(result)
                elif token == '-':
                    result = pop1 - pop2
                    stack.append(result)
                elif token == '*':
                    result = pop1 * pop2
                    stack.append(result)
                else:
                    result = pop1 // pop2
                    stack.append(result)
    print('#{} {}'.format(number+1, pop_clac))

