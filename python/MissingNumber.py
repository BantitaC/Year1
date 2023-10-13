'''MissingNumber'''
def missing(num, fixset):
    '''MissingNumber'''
    fix = int(input())
    fixset.add(fix)

    while fix != 0:
        fix = int(input())
        fixset.add(fix)

    for i in range(0, num + 1):
        if i not in fixset:
            print(i)

missing(int(input()), set())
