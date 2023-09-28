'''[Midterm 2022] Parity'''
def parity(num, choose):
    '''[Midterm 2022] Parity'''
    nub = 0
    for i in num:
        if i == "1":
            nub += 1
 
    if choose == "Even":
        if nub % 2 == 0:
            print(num + "0")
        else:
            print(num + "1")
    elif choose == "Odd":
        if nub % 2 == 0:
            print(num + "1")
        else:
            print(num + "0")
 
parity(input(), input())
