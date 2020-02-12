for number in range(10):
    word_len = int(input())
    palindrome_pan = [input() for i in range(8)]
    word_count = 0

    for i in range(8): #가로
        for j in range(8 - word_len + 1):

            count = 0
            if palindrome_pan[i][j] == palindrome_pan[i][j + word_len - 1]:
                count += 1

                for n in range(word_len // 2 - 1):
                    if palindrome_pan[i][j + 1 + n] == palindrome_pan[i][j + word_len - 2 - n]:
                        count += 1
                    else:
                        break

            if count == word_len // 2:
                word_count += 1

    for j in range(8):  # 세로
        for i in range(8 - word_len + 1):

            count = 0
            if palindrome_pan[i][j] == palindrome_pan[i + word_len - 1][j]:
                count += 1

                for n in range(word_len // 2 - 1):
                    if palindrome_pan[i + 1 + n][j] == palindrome_pan[i + word_len - 2 - n][j]:
                        count += 1
                    else:
                        break

            if count == word_len // 2:
                word_count += 1

    print('#{} {}'.format(number+1, word_count))