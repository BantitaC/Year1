'''[Recommend] Harshad Number'''
def harshad():
    '''[Recommend] Harshad Number'''
    for _ in range(10):
        num = int(input())
        if num == 0:
            print("No")
        elif len(str(num)) == 1:
            if num % num == 0:
                print("Yes")
            else:
                print("No")
        else:
            if num % sumnum(num) == 0:
                print("Yes")
            else:
                print("No")
def sumnum(num):
    """cal"""
    sumn = 0
    if num < 0:
        for i in str(num)[1:]:
            sumn += int(i)
        sumn *= -1
    else:
        for i in str(num):
            sumn += int(i)
    return sumn

harshad()
