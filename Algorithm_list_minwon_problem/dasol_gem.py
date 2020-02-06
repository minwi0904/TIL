numbers = int(input())
for number in range(numbers):
    gem = input()
    result = '#'
    if len(gem) == 1:
        print('..#..')
        print('.#.#.')
        print('#.' + gem + '.#')
        print('.#.#.')
        print('..#..')
    else:
        print('..#...', end ='')
        print('#...'*(len(gem)-2), end='')
        print('#..')
        print('.#.#' * len(gem) + '.')
        for i in range(len(gem)):
            result += '.'+gem[i]+'.#'
        print(result)
        print('.#.#' * len(gem) + '.')
        print('..#...' + '#...' * (len(gem) - 2) + '#..')

