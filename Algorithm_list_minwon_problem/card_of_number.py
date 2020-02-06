numbers = int(input())
for number in range(1, numbers+1):
    count = input()
    card_list = [0]*10
    card_numbers = input()
    for card_number in card_numbers:
        for i in range(10):
            if int(card_number) == i:
                card_list[i] += 1
    max_card = max(card_list)
    for i in range(9,-1,-1):
        if max_card == card_list[i]:
            da_number = i
            break
   
    print('#{} {} {}'.format(number, da_number ,max_card))


