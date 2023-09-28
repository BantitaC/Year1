'''[Midterm 2021] Squid Game'''
def squid():
    '''[Midterm 2021] Squid Game'''
    teama = 0
    teamb = 0
    for _ in range(10):
        aaa = int(input())
        teama += aaa
    for _ in range(10):
        bbb = int(input())
        teamb += bbb
 
    if teama > teamb:
        print("B")
    elif teamb > teama:
        print("A")
    else:
        print("AB")
 
squid()
