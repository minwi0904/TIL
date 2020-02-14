numbers = int(input())

for number in range(numbers):
    gumsa = input()
    gualho = []

    for g in gumsa:
        if g == '{' or g ==  '(':
            gualho.append(g)
        if g == '}':
            if gualho != [] and gualho[-1] == '{':
                gualho.pop()
            else:
                result = 0
                break
        if g == ')':
            if gualho != [] and gualho[-1] == '(':
                gualho.pop()
            else:
                result = 0
                break
    else:
        if gualho == []:
            result = 1
        else:
            result = 0

    print('#{} {}'.format(number+1, result))