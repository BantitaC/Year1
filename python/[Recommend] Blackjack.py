'''[Recommend] Blackjack'''
def blackjack(num):
    '''[Recommend] Blackjack'''
    point = 0
    keep = 0
    for i in range(num):
        i = i
        card = input()
        if card in "JQKjqk":
            point += 10
        elif card in "Aa":
            keep += 1
        else:
            point += int(card)
    while keep > 0:
        keep -= 1
        if point + 11 > 21:
            point += 1
        elif point == 10 and keep == 1:
            point += 1
        else:
            point += 11
    print(point)

blackjack(int(input()))
