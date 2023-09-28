'''[Recommend] Lotto'''
def lotto(first, back2, fore3_1, fore2, back3_1):
    '''[Recommend] Lotto'''
    back3_2 = input()
    mylotto = input()
    money = 0
    nearfirst1 = ""
    nearfirst2 = ""
    if first == "000000":
        nearfirst1 = "000001"
        nearfirst2 = "999999"
    elif first == "999999":
        nearfirst1 = "999998"
        nearfirst2 = "000000"
    else:
        nearfirst1 = ("%06d" %(int(first)-1))
        nearfirst2 = ("%06d" %(int(first)+1))
    if mylotto == first:
        money += 6000000
    if mylotto == nearfirst1 or mylotto == nearfirst2:
        money += 100000
    if mylotto[-2:] == back2:
        money += 2000
    if mylotto[:3] == fore3_1:
        money += 4000
    if mylotto[:3] == fore2:
        money += 4000
    if mylotto[-3:] == back3_1:
        money += 4000
    if mylotto[-3:] == back3_2:
        money += 4000
    print(money)

lotto(input(), input(), input(), input(), input())
