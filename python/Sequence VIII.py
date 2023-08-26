'''Sequence VIII'''
def sequence(num):
    '''Sequence VIII'''
    lst = []
    for i in range(1, num+1):
        lst.append(i)
        i += 2
        for j in range(0, len(lst)):
            print("%d" % lst[j], end=" ")
        print()

sequence(int(input()))
