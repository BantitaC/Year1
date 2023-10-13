'''MissingNumber (No Set)'''
def missing(num, fix, lst):
    '''MissingNumber (No Set)'''
    lst.append(fix)
    while fix != 0:
        fix = int(input())
        lst.append(fix)

    lst.sort()

    for i in range(0, num + 1):
        if i not in lst:
            print(i)

missing(int(input()), int(input()), [])
