for number in range(1, 11):
    N = int(input())
    calc = input()

    afterInput = {
        '+': 1,
        '*': 2,
        '(': 0
    }

    stack = []
    calc_list = []
    for token in calc:
        if token == '(':
            stack.append(token)

        elif token == ')':
            while True:
                pop = stack.pop()
                if pop == '(':
                    break
                else:
                    calc_list.append(pop)

        elif token.isdigit():
            calc_list.append(token)

        else:
            if stack and afterInput[token] > afterInput[stack[-1]]:
                stack.append(token)
            else:
                while True:
                    pop = stack.pop()
                    calc_list.append(pop)
                    if stack and afterInput[token] > afterInput[stack[-1]]:
                        stack.append(token)
                        break

    for calc in calc_list:
        if calc.isdigit():
            stack.append(calc)
        else:
            pop2 = int(stack.pop())
            pop1 = int(stack.pop())
            if calc == '+':
                result = pop1 + pop2
                stack.append(result)
            else:
                result = pop1 * pop2
                stack.append(result)

    print('#{} '.format(number), end = '')
    print(*stack)