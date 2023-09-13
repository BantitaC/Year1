'''Sequence IX'''
def sequence(row):
    '''Sequence IX'''
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
        print("\r")
 
sequence(int(input()))
