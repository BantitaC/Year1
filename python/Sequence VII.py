'''Sequence VIII'''
def sequence(row):
    '''Sequence VIII'''
    for col in range(0, row):
        num = 1
        for i in range(col + 1, row):
            print("  ", end=" ")
        for i in range(0, col + 1):
            i = i
            print("%02d" % num, end=" ")
            num += 1
        print("\r")
 
sequence(int(input()))
