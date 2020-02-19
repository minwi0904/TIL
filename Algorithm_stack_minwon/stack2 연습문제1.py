calc = input().split()
stack = []
out = []

token_isp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,
}

for token in calc:
    if token.isdigit() == True:
        out.append(token)
    else:
        if stack == []:
            stack.append(token)
        else:
            if token == '(':
                stack.append(token)
            elif token == ')':
                while True:
                    pop = stack.pop()
                    if pop == '(':
                        break
                    else:
                        out.append(pop)
            else:
                if token_isp[token] > token_isp[stack[-1]]:
                    stack.append(token)
                else:
                    while True:
                        if stack and token_isp[token] <= token_isp[stack[-1]]:
                            pop = stack.pop()
                            out.append(pop)
                        else:
                            break
                    stack.append(token)

while stack:
    pop = stack.pop()
    out.append(pop)

print(*out)

for i in out:
    if i.isdigit() == True:
        stack.append(i)
    else:
        calc2 = int(stack.pop())
        calc1 = int(stack.pop())
        if i == '-':
            result = calc1 - calc2
        elif i == '+':
            result = calc1 + calc2
        elif i == '*':
            result = calc1 * calc2
        else:
            result = calc1 / calc2

        stack.append(result)

print(*stack)