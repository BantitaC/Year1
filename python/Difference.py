'''Difference'''
def diff(num_n, num_m, user_setn, user_setm, keep):
    '''Difference'''
    for _ in range(num_n):
        nnn = int(input())
        user_setn.add(nnn)
 
    for _ in range(num_m):
        mmm = int(input())
        user_setm.add(mmm)
 
    anotb = user_setn.difference(user_setm)
    keep = sorted(anotb)
 
    for i in keep:
        print(i, end=" ")
 
diff(int(input()), int(input()), set(), set(), "")
