'''Sequence X'''
def sequence(row):
    '''Sequence X'''
    for col in range(row):
        num = 1
        for i in range(col + 1, row):
            print("  ", end=" ")
        for i in range(col + 1):
            i = i
            print("%02d" % num, end=" ")
            num += 1
        if i != 0:
            num = i
            for i in range(col):
                i = i
                print("%02d" % num, end=" ")
                num -= 1
        print()
    for col in range(row, 0, -1):
        num = 1
        for i in range(col - 1, row):
            print("  ", end=" ")
        for i in range(col - 1):
            print("%02d" % num, end=" ")
            num += 1
        num = col - 2
        for i in range(col, 2, -1):
            i = i
            print("%02d" % num, end=" ")
            num -= 1
        print()
 
sequence(int(input()))
