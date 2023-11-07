'''[Recommended] ATM'''
def atm(money):
    '''[Recommended] ATM'''
    while True:
        dnw = input().split()
        if dnw[0] == "END":
            break
        if dnw[0] == "D":
            money += int(dnw[1])
        elif dnw[0] == "W":
            if money > int(dnw[1]):
                money -= int(dnw[1])
            else:
                money -= money
    print(money)

atm(int(input()))
