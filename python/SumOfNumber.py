'''SumOfNumber'''
def allnum(total, num):
    '''SumOfNumber'''
    total1 = 0
    while True:
        num = int(input())
        if num == -1 or num == total:
            break
        total1 += num
    print(total1+1)

allnum(int(input()), int(input()))
